from fastapi import APIRouter, FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from configuration import database
from project import models,schemas,crud





models.Base.metadata.create_all(bind=database.engine)
app = APIRouter()

@app.post("/add_users", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/get_users", response_model=list[schemas.User])
async def get_users(db: Session = Depends(database.get_db)):
    return crud.get_users(db=db)

@app.patch("/update_users/{user_id}", response_model=schemas.User)
async def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(database.get_db)):
    return crud.update_user(db=db, user_id=user_id, user=user)

@app.delete("/delete_users/{user_id}", response_model=schemas.User)
async def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_user(db=db, user_id=user_id)
