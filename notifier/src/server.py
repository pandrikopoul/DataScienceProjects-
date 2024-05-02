import asyncio
import signal

import grpc
from google.protobuf import empty_pb2
from src.notifier import send_notification

from proto.notifier.notifier_pb2_grpc import (
    NotifierServiceServicer,
    add_NotifierServiceServicer_to_server,
)


class NotifierServicer(NotifierServiceServicer):
    async def SendNotification(self, request, _):
        await send_notification(
            notification_type=request.notification_type,
            researcher=request.researcher,
            measurement_id=request.measurement_id,
            experiment_id=request.experiment_id,
            cipher_data=request.cipher_data,
        )
        return empty_pb2.Empty()


async def serve():
    server = grpc.aio.server()
    add_NotifierServiceServicer_to_server(NotifierServicer(), server)
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
