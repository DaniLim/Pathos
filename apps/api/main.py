from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/posts', response_model=schemas.PostRead)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    db_post = models.Post(text=post.text)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@app.get('/posts', response_model=list[schemas.PostRead])
def list_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).order_by(models.Post.created_at.desc()).all()
