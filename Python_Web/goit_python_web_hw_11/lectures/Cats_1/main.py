import os
import pathlib
import time
from fastapi import Depends, FastAPI, HTTPException, Request, status, Path, File, UploadFile

from sqlalchemy import text
from sqlalchemy.orm import Session

from db import get_db

from middlewares import CustomRequestMiddleware
from schemas import CatResponse, CatSchema, OwnerResponse, OwnerSchema
from models import Owner, Cat

app = FastAPI()

@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app.add_middleware(CustomRequestMiddleware)

# ----------------------------------------------------------------
@app.get('/')
def main_root():
    return {"message": "Welcome to fastapi world"}


@app.get('/owners', response_model=list[OwnerResponse], tags=['owners'])
async def get_owners(db: Session = Depends(get_db)):
    owners = db.query(Owner).all()
    return owners


@app.post("/owners", response_model=OwnerResponse, tags=["owners"])
async def create_owner(body:OwnerSchema, db: Session = Depends(get_db)):
    owner = db.query(Owner).filter_by(email=body.email).first()
    if owner:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Owner already exists"
        )
    owner = Owner(fullname=body.fullname,email=body.email)
    db.add(owner)
    db.commit()
    db.refresh(owner)
    return owner


@app.put("/owners/{owner_id}", response_model=OwnerResponse, tags=["owners"])
async def update_owner(body: OwnerSchema, owner_id: int = Path(ge=1), db: Session = Depends(get_db)):
    owner = db.query(Owner).filter_by(id=owner_id).first()
    if owner is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Owner does not exists"
        )
    owner.fullname = body.fullname 
    owner.email= body.email
    db.commit()
    db.refresh(owner)
    return owner


@app.put("/owners/{owner_id}", response_model=OwnerResponse, tags=["owners"])
async def update_owner(body: OwnerSchema, owner_id: int = Path(ge=1), db: Session = Depends(get_db)):
    owner = db.query(Owner).filter_by(id=owner_id).first()
    if owner is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Owner does not exists"
        )
    owner.fullname = body.fullname 
    owner.email= body.email
    db.commit()
    db.refresh(owner)
    return owner


@app.get("/owners/{owner_id}", response_model=OwnerResponse, tags=["owners"])
async def get_owner_by_id(
    owner_id: int = Path(ge=1), db: Session = Depends(get_db)
):
    owner = db.query(Owner).filter_by(id=owner_id).first()
    if owner is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Owner does not exists"
        )
    return owner

@app.put("/owners/{owner_id}", response_model=OwnerResponse, tags=["owners"])
async def update_owner(body: OwnerSchema, owner_id: int = Path(ge=1), db: Session = Depends(get_db)):
    owner = db.query(Owner).filter_by(id=owner_id).first()
    if owner is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Owner does not exists"
        )
    owner.fullname = body.fullname 
    owner.email= body.email
    db.commit()
    db.refresh(owner)
    return owner


@app.delete("/owners/{owner_id}", response_model=OwnerResponse, tags=["owners"])
async def delete_owner(owner_id: int = Path(ge=1), db: Session = Depends(get_db)):
    owner = db.query(Owner).filter_by(id=owner_id).first()
    if owner is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Owner does not exists"
        )
    db.delete(owner)
    db.commit()
    return owner

# ----------------------------------------------------------------
@app.get("/cats", response_model=list[CatResponse], tags=["cats"])
async def get_cats(db: Session = Depends(get_db)):
    cats = db.query(Cat).all()
    return cats


@app.get("/cats/{cat_id}", response_model=CatResponse, tags=["cats"])
async def get_cat_by_id(cat_id: int = Path(ge=1), db: Session = Depends(get_db)):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Owner does not exists"
        )
    return cat


@app.post("/cats", response_model=CatResponse, tags=["cats"])
async def create_cat(body: CatSchema, db: Session = Depends(get_db)):
    
    cat=Cat(**body.model_dump())
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat


@app.put("/cats/{cat_id}", response_model=CatResponse, tags=["cats"])
async def update_cat(
    body: CatSchema, cat_id: int = Path(ge=1), db: Session = Depends(get_db)
):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cat does not exists"
        )
    cat.nick = body.nick
    cat.age = body.age
    cat.vacinated = body.vacinated
    cat.owner_id =  body.owner_id
    db.commit()
    db.refresh(cat)
    return cat


@app.delete("/cats/{cat_id}", response_model=CatResponse, tags=["cats"])
async def delete_cat(cat_id: int = Path(ge=1), db: Session = Depends(get_db)):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cat does not exists"
        )
    db.delete(cat)
    db.commit()
    return cat


@app.get('/api/healthchecker')
def healthchecker(db: Session = Depends(get_db)):
    try:
        result = db.execute(text('SELECT 1')).fetchone()
        if result is None:
            raise HTTPException(
                status_code=500, detail="Database is not configured correctly"
            )   
        return {'message':'Welcome to fastapi'}
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, detail="Error connecting to database"
        )

MAX_FILE_SIZE = 1024 * 1024 * 3 # 3 mb
@app.post('/upload-file')
async def create_upload_file(file: UploadFile = File()):
    pathlib.Path('uploads').mkdir(exist_ok=True)
    file_path = f'uploads/{file.filename}'
    file_size = 0

    with open(file_path, 'wb') as f:
        while True:
            chunk = await file.read(1024)
            if not chunk:
                break
        file_size += len(chunk)
        if file_size > MAX_FILE_SIZE:
            f.close()
            os.remove(file_path)
            # pathlib.Path(file_path).unlink() - alternative solution to remove file
            raise HTTPException(
                status_code=413,
                detail=f"File too large. File must be smaller than {MAX_FILE_SIZE / 1024 / 1024} MB",
            )
        f.write(chunk)

    return {"file_path": file_path}
