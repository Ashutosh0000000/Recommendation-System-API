# app/seed.py
import asyncio
from random import choice
from sqlalchemy import select
from .database import async_session, init_db, Base, engine
from . import models

async def clear_db():
    """Drop all tables and recreate them."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("Database cleared and recreated.")

async def seed_demo():
    await clear_db()
    async with async_session() as db:
        # -------------------
        # Add items explicitly
        # -------------------
        items_to_add = ["Item 1", "Item 2", "Item 3"]
        for item_name in items_to_add:
            db.add(models.Item(name=item_name))
        await db.commit()

        # -------------------
        # Add users
        # -------------------
        users_to_add = ["user1@example.com", "user2@example.com", "user3@example.com"]
        for email in users_to_add:
            user = models.User(email=email, password="hashed")
            db.add(user)
        await db.commit()

        # -------------------
        # Add activities
        # -------------------
        # Use ORM select to get full objects
        all_users = await db.execute(select(models.User))
        users = all_users.scalars().all()
        all_items = await db.execute(select(models.Item))
        items = all_items.scalars().all()

        actions = ["viewed", "clicked", "purchased"]

        for user in users:
            for _ in range(3):  # 3 activities per user
                activity = models.Activity(
                    user_id=user.id,
                    item_id=choice(items).id,
                    action=choice(actions)
                )
                db.add(activity)
        await db.commit()
    print("Database seeded successfully!")

if __name__ == "__main__":
    asyncio.run(seed_demo())
