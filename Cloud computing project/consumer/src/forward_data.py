import asyncio
from enum import Enum
import logging
import grpc

from proto.database_gateway.database_gateway_pb2 import AddTemperatureRequest
from proto.database_gateway.database_gateway_pb2_grpc import DBGatewayServiceStub
from proto.notifier.notifier_pb2 import NotifierRequest
from proto.notifier.notifier_pb2_grpc import NotifierServiceStub


class NotificationType(str, Enum):
    OUT_OF_RANGE = "OutOfRange"
    STABLE = "Stabilized"


async def notification_task(notifier_request: NotifierRequest):
    try:
        async with grpc.aio.insecure_channel("notifier:50051") as channel:
            stub = NotifierServiceStub(channel)
            await stub.SendNotification(notifier_request, timeout=5)
    except Exception as e:
        logging.error(f"Failed to send notification: {e}")


def notify(
    notification_type: NotificationType,
    researcher: str,
    measurement_id: str,
    experiment_id: str,
    cipher_data: str,
    background_loop: asyncio.AbstractEventLoop,
):
    async def create_task():
        notifier_request = NotifierRequest(
            notification_type=notification_type,
            researcher=researcher,
            measurement_id=measurement_id,
            experiment_id=experiment_id,
            cipher_data=cipher_data,
        )

        await notification_task(notifier_request)

    background_loop.call_soon_threadsafe(
        lambda: background_loop.create_task(create_task())
    )


async def save_temperature_to_db_task(add_temperature_request: AddTemperatureRequest):
    try:
        async with grpc.aio.insecure_channel("database-gateway:50051") as channel:
            stub = DBGatewayServiceStub(channel)
            await stub.AddTemperature(add_temperature_request, timeout=5)
    except Exception as e:
        logging.error(f"Failed to send notification: {e}")


def save_temperature_to_db(
    experiment_id: str,
    out_of_bounds: bool,
    timestamp: float,
    temperature: float,
    background_loop: asyncio.AbstractEventLoop,
):
    async def create_task():
        add_temperature_request = AddTemperatureRequest(
            experiment_id=experiment_id,
            out_of_bounds=out_of_bounds,
            timestamp=timestamp,
            temperature=temperature,
        )

        await save_temperature_to_db_task(
            add_temperature_request=add_temperature_request
        )

    background_loop.call_soon_threadsafe(
        lambda: background_loop.create_task(create_task())
    )
