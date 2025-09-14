# app/migrate.py
from app.database import engine, Base
import asyncio

async def run_migrations():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(run_migrations())
