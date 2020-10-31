from sqlalchemy.orm import Session

from . import models
from app import schemas

def get_all_profiles(db: Session):
    return db.query(models.Profile).all()


def get_profile_by_id(db: Session, profile_id: int):
    return db.query(models.Profile).filter(models.Profile.id == profile_id).first()


def create_profile(db: Session, profil: schemas.CreateProfile):
    db_profil = models.Profile(**profil.dict())
    db.add(db_profil)
    db.commit()
    db.refresh(db_profil)
    return db_profil