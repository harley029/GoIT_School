from sqlalchemy.exc import SQLAlchemyError

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from src.conf.config import config

engine = create_async_engine(config.DB_URL)
local_session = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def get_db():
    try:
        async with local_session() as session:
            yield session
    except SQLAlchemyError as e:
        # Логування помилки або інші дії
        print(f"Database session creation failed: {e}")
        raise HTTPException(status_code=500, detail="Database session creation failed")
