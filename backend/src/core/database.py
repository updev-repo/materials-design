from motor.motor_asyncio import AsyncIOMotorClient

from src.core.config import settings

client: AsyncIOMotorClient | None = None


async def get_database():
    """Get MongoDB database instance."""
    return client[settings.mongodb_db_name]


async def connect_to_mongodb() -> None:
    """Connect to MongoDB."""
    global client
    client = AsyncIOMotorClient(settings.mongodb_url)


async def close_mongodb_connection() -> None:
    """Close MongoDB connection."""
    global client
    if client:
        client.close()
        client = None
