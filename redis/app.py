import asyncio

import aioredis


async def main():
    # Redis client bound to single connection (no auto reconnection).
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_responses=True
    )
    # async with redis.client() as conn:
    val = await redis.get("users:1")
    # await redis.expire("users:1", 10)
    print(f" -> {val}")


if __name__ == "__main__":
    asyncio.run(main())

