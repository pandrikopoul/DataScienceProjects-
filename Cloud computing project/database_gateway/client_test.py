import asyncio

import grpc
from proto.database_gateway_pb2 import (
    AddTemperatureRequest,
    QueryOutOfRangeRequest,
    QueryTemperatureRequest,
)
from proto.database_gateway_pb2_grpc import DBGatewayServiceStub


async def run():
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = DBGatewayServiceStub(channel)

        out_of_range_request = QueryOutOfRangeRequest(experiment_id="123")
        out_of_range_response = await stub.QueryOutOfRange(out_of_range_request)
        print("QueryOutOfRange Response:", out_of_range_response)

        temp_request = QueryTemperatureRequest(
            experiment_id="123", start_epoch_time=0, end_epoch_time=999999
        )
        temp_response = await stub.QueryTemperature(temp_request)
        print("QueryTemperature Response:", temp_response)

        add_temp_request = AddTemperatureRequest(
            experiment_id="123",
            out_of_bounds=True,
            timestamp=1622559642,
            temperature=25.6,
        )
        add_temp_response = await stub.AddTemperature(add_temp_request)
        print("AddTemperature Response:", add_temp_response)


if __name__ == "__main__":
    asyncio.run(run())
