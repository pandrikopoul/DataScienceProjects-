import asyncio
import signal

import grpc
from google.protobuf import empty_pb2
from src.database_gateway import add_temperature, query_out_of_range, query_temperature

from proto.database_gateway.database_gateway_pb2 import (
    AddTemperatureRequest,
    QueryOutOfRangeRequest,
    QueryOutOfRangeResponse,
    QueryTemperatureRequest,
    QueryTemperatureResponse,
    TemperatureRecord,
)
from proto.database_gateway.database_gateway_pb2_grpc import (
    DBGatewayServiceServicer,
    add_DBGatewayServiceServicer_to_server,
)

from motor.motor_asyncio import AsyncIOMotorClient
import pymongo


class DBGatewayService(DBGatewayServiceServicer):
    async def QueryOutOfRange(self, request: QueryOutOfRangeRequest, _):
        records = await query_out_of_range(request.experiment_id)
        return QueryOutOfRangeResponse(
            temperatures=[
                TemperatureRecord(
                    timestamp=rec["timestamp"], temperature=rec["temperature"]
                )
                for rec in records
            ]
        )

    async def QueryTemperature(self, request: QueryTemperatureRequest, _):
        records = await query_temperature(
            request.experiment_id, request.start_epoch_time, request.end_epoch_time
        )
        return QueryTemperatureResponse(
            temperatures=[
                TemperatureRecord(
                    timestamp=rec["timestamp"], temperature=rec["temperature"]
                )
                for rec in records
            ]
        )

    async def AddTemperature(self, request: AddTemperatureRequest, _):
        await add_temperature(
            request.experiment_id,
            request.out_of_bounds,
            request.timestamp,
            request.temperature,
        )
        return empty_pb2.Empty()


async def _setup_mongo():
    client = AsyncIOMotorClient("mongodb://mongo:27017/")
    db = client["temperature_db"]
    await db.collection.create_index(
        [("experiment_id", pymongo.ASCENDING), ("out_of_bounds", pymongo.ASCENDING)]
    )
    await db.collection.create_index(
        [("experiment_id", pymongo.ASCENDING), ("timestamp", pymongo.ASCENDING)]
    )


async def serve():
    await _setup_mongo()
    server = grpc.aio.server()
    add_DBGatewayServiceServicer_to_server(DBGatewayService(), server)
    server.add_insecure_port("[::]:50051")
    await server.start()

    loop = asyncio.get_running_loop()

    def stop_server():
        loop.create_task(server.stop(None))

    loop.add_signal_handler(signal.SIGINT, stop_server)
    loop.add_signal_handler(signal.SIGTERM, stop_server)

    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())
