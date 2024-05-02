import asyncio

import grpc
from proto.notifier.notifier_pb2 import NotifierRequest
from proto.notifier.notifier_pb2_grpc import NotifierServiceStub


async def send_notification(stub):
    await stub.SendNotification(
        NotifierRequest(
            notification_type="OutOfRange",
            researcher="d.landau@uu.nl",
            measurement_id="1234",
            experiment_id="5678",
            cipher_data="D5qnEHeIrTYmLwYX.hSZNb3xxQ9MtGhRP7E52yv2seWo4tUxYe28ATJVHUi0J++SFyfq5LQc0sTmiS4ILiM0/YsPHgp5fQKuRuuHLSyLA1WR9YIRS6nYrokZ68u4OLC4j26JW/QpiGmAydGKPIvV2ImD8t1NOUrejbnp/cmbMDUKO1hbXGPfD7oTvvk6JQVBAxSPVB96jDv7C4sGTmuEDZPoIpojcTBFP2xA",
        )
    )


async def run():
    async with grpc.aio.insecure_channel("notifier:50051") as channel:
        stub = NotifierServiceStub(channel)

        tasks = [asyncio.create_task(send_notification(stub)) for _ in range(100)]

        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(run())
