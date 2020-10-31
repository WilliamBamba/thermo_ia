from typing import List

from fastapi import APIRouter, Request, Depends, HTTPException

from app import schemas
from app.database import crud, config
from sqlalchemy.orm import Session

router = APIRouter()


@router.get('/', response_model=List[schemas.Profile])
def get_profiles(db: Session = Depends(config.get_db)):
    return crud.get_all_profiles(db)


@router.get('/{profile_id}', response_model=schemas.Profile)
def get_profile(profile_id: int, db: Session = Depends(config.get_db)):
    profile = crud.get_profile_by_id(db, profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@router.post('/', response_model=schemas.Profile)
def create_profile(profile: schemas.CreateProfile, db: Session = Depends(config.get_db)):
    return crud.create_profile(db, profile)

