from app.database import models
from typing import List

from fastapi import APIRouter, Request, Depends, HTTPException

from app import schemas
from app.database import crud, config
from sqlalchemy.orm import Session

router = APIRouter()


@router.get('/', response_model=List[schemas.Profile])
def get_profiles(db: Session = Depends(config.get_db)):
    return crud.get_all(db, models.Profile)


@router.get('/{profile_id}', response_model=schemas.Profile)
def get_profile(profile_id: int, db: Session = Depends(config.get_db)):
    profile = crud.get_profile_by_id(db, profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


# TODO: à modifier
@router.post('/', response_model=schemas.Profile)
def create_profile(profile: schemas.CreateProfile, db: Session = Depends(config.get_db)):
    return crud.create_profile(db, profile)



@router.get('/{profile_id}/link/{option_id}')
def link_option(profile_id: int, option_id: int, db: Session = Depends(config.get_db)):
    profile = crud.get_profile_by_id(db, profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    option = crud.get_option_by_id(db, option_id)
    if option is None:
        raise HTTPException(status_code=404, detail="Option not found")    

    crud.update_profile(db, profile_id, {'option_id': option_id})
    


# TODO: à modifier
@router.get('/{profile_id}/link/{agenda_id}')
def link_agenda(profile_id: int, agenda_id: int, db: Session = Depends(config.get_db)):
    # TODO: verify profile & agenda exists
    crud.update_profile(db, profile_id, {'agenda_id': agenda_id})
    