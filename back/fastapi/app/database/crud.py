from app.routes import profile
from sqlalchemy.orm import Session
from sqlalchemy import desc

from . import models
from app import schemas


def get_all(db: Session, model):
    return db.query(model).all()

def get_model_by_id(db: Session, model_id: int, model):
    return db.query(model).filter(model.id == model_id).first()

def get_most_recent_model(db: Session, model):
    return db.query(model).order_by(desc('created_at')).first()

def update_model(db: Session, model_id: int, model, new_data: dict):
    db.query(model).filter(model.id == model_id).update(new_data)
    db.commit()

def delete_model(db: Session, model_id: int, model):
    db.query(model).filter(model.id == model_id).delete()
    db.commit()

def create_model(db: Session, model, data):
    db_model = model(**data.dict())
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model