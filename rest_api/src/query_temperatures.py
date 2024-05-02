from src.data_models import TemperatureMeasurement

from proto.database_gateway.database_gateway_pb2 import (
    QueryOutOfRangeRequest,
    QueryTemperatureRequest,
)
from proto.database_gateway.database_gateway_pb2_grpc import DBGatewayServiceStub


async def temperatures(
    experiment_id: str,
    start_time: float,
    end_time: float,
    grpc_stub: DBGatewayServiceStub,
):
    temp_request = QueryTemperatureRequest(
        experiment_id=experiment_id,
        start_epoch_time=start_time,
        end_epoch_time=end_time,
    )
    temp_response = await grpc_stub.QueryTemperature(temp_request)
    return [
        TemperatureMeasurement(timestamp=rec.timestamp, temperature=rec.temperature)
        for rec in temp_response.temperatures
    ]


async def temperatures_out_of_range(
    experiment_id: str,
    grpc_stub: DBGatewayServiceStub,
):
    out_of_range_request = QueryOutOfRangeRequest(experiment_id=experiment_id)
    out_of_range_response = await grpc_stub.QueryOutOfRange(out_of_range_request)
    return [
        TemperatureMeasurement(timestamp=rec.timestamp, temperature=rec.temperature)
        for rec in out_of_range_response.temperatures
    ]
