from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import text

from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.routes import todos

app = FastAPI()
app.include_router(todos.router, prefix='/api')

@app.get('/')
def index():
    return {'message': 'ToDo application'}


@app.get("/api/healthchecker")
async def healthchecker(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT 1"))
        result = result.fetchone()
        if result is None:
            raise HTTPException(
                status_code=500, detail="Database is not configured correctly"
            )
        return {"message": "Welcome to fastapi"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to database")
