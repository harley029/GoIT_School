from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.entity.models import Todo
from src.schemas.todo import TodoSchema, TodoUpdateSchema


async def get_todos(limit: int, offset: int, db: AsyncSession):
    stmt = select(Todo).offset(offset).limit(limit)
    result = await db.execute(stmt)
    todos = result.scalars().all()
    return todos


async def get_todo(todo_id: int, db: AsyncSession):
    stmt = select(Todo).filter_by(id=todo_id)
    result = await db.execute(stmt)
    todo = result.scalar_one_or_none()
    return todo


async def create_todo(body: TodoSchema, db: AsyncSession):
    todo = Todo(**body.model_dump())
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return todo


async def update_todo(todo_id: int, body: TodoUpdateSchema, db: AsyncSession):
    stmt = select(Todo).filter_by(id=todo_id)
    result = await db.execute(stmt)
    todo = result.scalar_one_or_none()
    if todo is None:
        return None
    for key, value in body.model_dump().items():
        setattr(todo, key, value)
    await db.commit()
    await db.refresh(todo)
    return todo


async def delete_todo(todo_id: int, db: AsyncSession):
    stmt = select(Todo).filter_by(id=todo_id)
    result = await db.execute(stmt)
    todo = result.scalar_one_or_none()
    if todo:
        await db.delete(todo)
        await db.commit()
    return todo
