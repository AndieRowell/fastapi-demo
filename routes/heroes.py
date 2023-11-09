from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from database import SessionLocal
import schemas
import crud

router = APIRouter(
    prefix="/heroes"
)

def get_db():
    db = SessionLocal()
    try:
        yield db #yield - kinda like return?
    finally:
        db.close()

@router.get("/all", response_model=List[schemas.HeroModel]) #extention of the prefix above - aka heroes/all
def get_heroes(db: Session = Depends(get_db)):

    #create a get crud operation to return the list of heroes
    # db.query(models.User).offset(skip).limit(limit).all()
        #want to run a db query to get all the users
    heroes = crud.get_heroes(db)
    return heroes
