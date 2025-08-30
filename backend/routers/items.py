from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import get_db

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.post("/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)

@router.get("/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_items(db, skip=skip, limit=limit)
