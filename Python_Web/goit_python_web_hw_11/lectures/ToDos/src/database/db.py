import contextlib
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine
from src.conf.config import config

class DatabaseSessionManager:
    def __init__(self, url: str):
        self._engine: AsyncEngine = create_async_engine(url)
        self._session_maker: async_sessionmaker = async_sessionmaker(
            autoflush=False, autocommit=False, bind=self._engine
        )

    @contextlib.asynccontextmanager
    async def session(self):
        async with self._session_maker() as session:
            try:
                yield session
            except Exception as e:
                print(e)
                await session.rollback()
            finally:
                await session.close()

sessionmanager = DatabaseSessionManager(config.DB_URL)

async def get_db():
    async with sessionmanager.session() as session:
        yield session
