from typing import List

import grpc

from fastapi import FastAPI, Query
from fastapi.responses import ORJSONResponse
from proto.database_gateway.database_gateway_pb2_grpc import DBGatewayServiceStub
from src.data_models import TemperatureMeasurement
from src.query_temperatures import (
    temperatures,
    temperatures_out_of_range,
)

app = FastAPI()

channel = None
stub = None


@app.get(
    "/temperature",
    response_model=List[TemperatureMeasurement],
    response_class=ORJSONResponse,
)
async def temperature(
    experiment_id: str = Query(..., alias="experiment-id"),
    start_time: float = Query(..., alias="start-time"),
    end_time: float = Query(..., alias="end-time"),
):
    return await temperatures(
        experiment_id=experiment_id,
        start_time=start_time,
        end_time=end_time,
        grpc_stub=stub,
    )


@app.get(
    "/temperature/out-of-range",
    response_model=List[TemperatureMeasurement],
    response_class=ORJSONResponse,
)
async def temperature_out_of_range(
    experiment_id: str = Query(..., alias="experiment-id"),
):
    return await temperatures_out_of_range(experiment_id=experiment_id, grpc_stub=stub)


@app.on_event("startup")
async def startup_event():
    global channel, stub
    channel = grpc.aio.insecure_channel("database-gateway:50051")
    stub = DBGatewayServiceStub(channel)


@app.on_event("shutdown")
async def shutdown_event():
    await channel.close()
