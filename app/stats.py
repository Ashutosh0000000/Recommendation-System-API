from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from collections import Counter
from . import models, schemas
from .database import get_db
from .dependencies import get_current_user

router = APIRouter(prefix="/api/stats", tags=["stats"])

MIN_ACTIVITIES = 3  # minimum activities to consider user "clean"

@router.get("/", response_model=schemas.UserStats)
async def get_stats(
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    # Optional: check if user is dirty based on activity count
    stmt_count = select(func.count(models.Activity.id))\
        .where(models.Activity.user_id == current_user.id)
    result_count = await db.execute(stmt_count)
    total_activities = result_count.scalar() or 0

    # Mark user as dirty if they have fewer than MIN_ACTIVITIES
    if total_activities < MIN_ACTIVITIES:
        current_user.is_dirty = True
    else:
        current_user.is_dirty = False

    # Commit dirty flag change (optional)
    db.add(current_user)
    await db.commit()
    await db.refresh(current_user)

    # Fetch activities regardless of dirty flag for stats
    stmt = select(func.count(models.Activity.id), models.Activity.item_id)\
        .where(models.Activity.user_id == current_user.id)\
        .group_by(models.Activity.item_id)
    result = await db.execute(stmt)
    rows = result.all()

    item_counts = Counter({item_id: count for count, item_id in rows})
    top_items = [item for item, _ in item_counts.most_common(5)]

    return schemas.UserStats(
        user_id=current_user.id,
        total_activities=total_activities,
        top_items=top_items
    )
