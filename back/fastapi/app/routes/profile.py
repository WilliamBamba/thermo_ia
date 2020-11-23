from app.database import models
from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app import schemas
from app.database import crud, config
from sqlalchemy.orm import Session

router = APIRouter()

#### TODO: mettre les bonnnes HTTP status


@router.get('/', response_model=List[schemas.Profile])
def get_profiles(db: Session = Depends(config.get_db)):
    return crud.get_all(db, models.Profile)


@router.get('/{profile_id}', response_model=schemas.Profile)
def get_profile(profile_id: int, db: Session = Depends(config.get_db)):
    profile = crud.get_model_by_id(db, profile_id, models.Profile)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@router.post('/', response_model=schemas.Profile)
def create_profile(profile: schemas.CreateProfile, db: Session = Depends(config.get_db)):
    return crud.create_model(db, models.Profile, profile)


@router.put('/{profile_id}', response_model=schemas.Profile)
def update_profile(profile_id: int, new_profile: schemas.UpdateProfile , db: Session = Depends(config.get_db)):
    profile = crud.get_model_by_id(db, profile_id, models.Profile)

    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")

    # TODO: refresh time_table from agenda url if provided

    crud.update_model(db, profile_id, models.Profile, new_profile)
    return crud.get_model_by_id(db, profile_id, models.Profile)


@router.delete('/{profile_id}')
def delete_profile(profile_id: int, db: Session = Depends(config.get_db)):
    profile = crud.get_model_by_id(db, profile_id, models.Profile)

    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")

    # TODO: refresh time_table from agenda url if provided

    crud.delete_model(db, profile_id, models.Profile)
    return 