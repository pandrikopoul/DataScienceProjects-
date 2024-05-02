import asyncio
import logging
import time
from typing import Final

from aiohttp import ClientSession

with open("./auth/token", mode="r") as f:
    token = f.read()

SERVICE_URL: Final = (
    "https://notifications-service.cc2023.4400app.me/api/notify?token=" + token
)
MAX_TIMEOUT: Final = 120


# Configure the logging settings
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def _exponential_backoff():
    """generator that yields exponential backoff times"""
    delay = 1
    while True:
        yield min(delay, MAX_TIMEOUT)
        delay *= 2


async def send_notification(
    notification_type: str,
    researcher: str,
    measurement_id: str,
    experiment_id: str,
    cipher_data: str,
) -> None:
    request_data = {
        "notification_type": notification_type,
        "researcher": researcher,
        "measurement_id": measurement_id,
        "experiment_id": experiment_id,
        "cipher_data": cipher_data,
    }

    async with ClientSession() as session:
        async with session.post(SERVICE_URL, json=request_data) as response:
            response_text = await response.text()

            # 2XX response
            if response.status // 100 == 2:
                logging.debug(f"Response from notification-service: {response_text}")

                return
            # 5XX response
            elif response.status // 100 == 5:
                logging.warning(
                    f"Request to {SERVICE_URL} failed with {response.status} {response_text}. Retrying..."
                )

                backoff = _exponential_backoff()
                start_time = time.time()
                while (time.time() - start_time) < MAX_TIMEOUT or (
                    not response.status // 100 == 5
                ):
                    await asyncio.sleep(next(backoff))
                    async with session.post(SERVICE_URL, json=request_data) as response:
                        response_text = await response.text()
                        if response.status // 100 == 2:
                            logging.debug(
                                f"Response from notification-service: {response_text}"
                            )
                            return
                        else:
                            logging.error(
                                f"Request to {SERVICE_URL} failed with status code {response.status} {response_text}"
                            )
                            return
            else:
                logging.error(
                    f"Request to {SERVICE_URL} failed with status code {response.status} {response_text}"
                )
                return
