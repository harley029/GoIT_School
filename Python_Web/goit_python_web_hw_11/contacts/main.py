import time
from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy import text

from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.routes import contacts

app = FastAPI()
app.include_router(contacts.router, prefix='/api')


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/")
def read_root():
    return {"message": "Contacts database, version 1.0"}


@app.get("/api/healthchecker")
async def healthchecker(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT 1"))
        result = result.fetchone()
        if result is None:
            raise HTTPException(
                status_code=500, detail="Database is not configured correctly"
            )
        return {"message": "Connection to database is established. Welcome to fastapi"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to database")
