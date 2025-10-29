from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config

MONGO_URI = config("MONGO_URI", default="")
MONGO_DB_NAME = config("MONGO_DB_NAME", default="")

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB_NAME]