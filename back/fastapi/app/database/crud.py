from app.routes import profile
from sqlalchemy.orm import Session

from . import models
from app import schemas


def get_all(db: Session, model):
    return db.query(model).all()


def get_profile_by_id(db: Session, profile_id: int):
    return db.query(models.Profile).filter(models.Profile.id == profile_id).first()


def create_profile(db: Session, profil: schemas.CreateProfile):
    db_profil = models.Profile(**profil.dict())
    db.add(db_profil)
    db.commit()
    db.refresh(db_profil)
    return db_profil


def update_profile(db: Session, profile_id: int, values: dict):

    db.query(models.Profile).filter(models.Profile.id == profile_id).update(values)




def create_agenda(db: Session, agenda: schemas.CreateAgenda):
    db_agenda = models.Agenda(**agenda.dict())
    db.add(db_agenda)
    db.commit()
    db.refresh(db_agenda)
    return db_agenda