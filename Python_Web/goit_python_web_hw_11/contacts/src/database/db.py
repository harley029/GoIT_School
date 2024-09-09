from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from src.conf.config import config

engine = create_async_engine(config.DB_URL)
local_session = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def get_db():
    async with local_session() as session:
        yield session
