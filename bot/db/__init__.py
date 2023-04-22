from contextlib import asynccontextmanager
from typing import AsyncContextManager

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

import bot.settings as settings

from .models import (
    Base,
    Client,
    Deal,
    Item,
    Skin,
    Container,
    Tool,
    Price,
    PriceLimit,
    Sticker,
    Agent,
)


DB_ADDR = (
    f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@"
    f"{settings.POSTGRES_HOST}/{settings.POSTGRES_DB}"
)

async_engine = create_async_engine(DB_ADDR, echo=False)


@asynccontextmanager
async def get_async_session(**kwargs) -> AsyncContextManager[AsyncSession]:
    session = AsyncSession(bind=async_engine, expire_on_commit=False, **kwargs)
    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()


__all__ = (
    "Base",
    "Client",
    "Deal",
    "Item",
    "Skin",
    "Container",
    "Tool",
    "Price",
    "PriceLimit",
    "Sticker",
    "Agent",
    "get_async_session",
    "DB_ADDR",
)
