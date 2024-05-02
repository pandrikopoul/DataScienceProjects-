from motor.motor_asyncio import AsyncIOMotorClient
import logging


client = AsyncIOMotorClient("mongodb://mongo:27017/")
db = client["temperature_db"]

logging.basicConfig(level=logging.ERROR)


async def query_out_of_range(experiment_id: str):
    cursor = db.collection.find(
        {"experiment_id": experiment_id, "out_of_bounds": True},
        {"timestamp": 1, "temperature": 1, "_id": False},
    )
    return await cursor.to_list(length=1000)


async def query_temperature(
    experiment_id: str, start_epoch_time: float, end_epoch_time: float
):
    cursor = db.collection.find(
        {
            "experiment_id": experiment_id,
            "timestamp": {"$gte": start_epoch_time, "$lte": end_epoch_time},
        },
        {"timestamp": 1, "temperature": 1, "_id": False},
    )
    return await cursor.to_list(length=1000)


async def add_temperature(
    experiment_id: str, out_of_bounds: bool, timestamp: str, temperature: float
):
    logging.debug(str(timestamp))
    await db.collection.insert_one(
        {
            "experiment_id": experiment_id,
            "out_of_bounds": out_of_bounds,
            "timestamp": timestamp,
            "temperature": temperature,
        }
    )
