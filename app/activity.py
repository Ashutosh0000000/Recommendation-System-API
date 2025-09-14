from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from . import models, schemas
from .database import get_db
from .dependencies import get_current_user

router = APIRouter(prefix="/api/activity", tags=["activity"])

@router.post("/", response_model=schemas.ActivityRead)
async def create_activity(
    activity: schemas.ActivityCreate,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user),  # require auth
):
    # 1️⃣ Check if the item exists
    result = await db.execute(select(models.Item).where(models.Item.id == activity.item_id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # 2️⃣ Count the user's activities
    count_result = await db.execute(
        select(func.count(models.Activity.id))
        .where(models.Activity.user_id == current_user.id)
    )
    activity_count = count_result.scalar()
    
    # 3️⃣ Mark user as dirty if less than 3 activities
    if activity_count < 3:
        current_user.is_dirty = True
        db.add(current_user)
        await db.commit()
        await db.refresh(current_user)
    
    # 4️⃣ Add the new activity
    db_activity = models.Activity(
        user_id=current_user.id,
        item_id=activity.item_id,
        action=activity.action
    )
    db.add(db_activity)
    await db.commit()
    await db.refresh(db_activity)
    return db_activity
