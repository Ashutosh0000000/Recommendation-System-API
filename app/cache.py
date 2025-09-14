import redis.asyncio as redis

# Create Redis connection
redis_client = redis.from_url("redis://localhost:6379", decode_responses=True)

async def get_redis():
    return redis_client

async def set_cache(key: str, value: str, expire: int = 3600):
    await redis_client.set(key, value, ex=expire)

async def get_cache(key: str):
    return await redis_client.get(key)

async def delete_cache_keys(*keys):
    if keys:
        await redis_client.delete(*keys)
