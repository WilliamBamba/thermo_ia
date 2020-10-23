from sqlalchemy.orm import Session

from . import models
from app import schemas

def create_user(db: Session, user: schemas.CreateProfil):
    profil = models.Profil(name=user.name)
    db.add(profil)
    db.commit()
    db.refresh(user)
    return user