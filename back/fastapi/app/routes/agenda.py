from app.database import models
from typing import List

from fastapi import APIRouter, Request, Depends, HTTPException

from app import schemas
from app.database import crud, config
from sqlalchemy.orm import Session

router = APIRouter()



@router.post('/', response_model=schemas.Agenda)
def create_agenda(agenda: schemas.CreateAgenda, db: Session = Depends(config.get_db)):
    return crud.create_agenda(db, agenda)



@router.get('/', response_model=List[schemas.Agenda])
def get_agendas(db: Session = Depends(config.get_db)):
    return crud.get_all(db, models.Agenda)


# @router.get('/{profile_id}', response_model=schemas.Profile)
# def get_profile(profile_id: int, db: Session = Depends(config.get_db)):
#     profile = crud.get_profile_by_id(db, profile_id)
#     if profile is None:
#         raise HTTPException(status_code=404, detail="Profile not found")
#     return profile



# @router.get('/{profile_id}/link/{option_id}')
# def link_option(profile_id: int, option_id: int, db: Session = Depends(config.get_db)):
#     # TODO: verify profile & option exists
#     crud.update_profile(db, profile_id, {'option_id': option_id})
    

# @router.get('/{profile_id}/link/{agenda_id}')
# def link_agenda(profile_id: int, agenda_id: int, db: Session = Depends(config.get_db)):
#     # TODO: verify profile & agenda exists
#     crud.update_profile(db, profile_id, {'agenda_id': agenda_id})
    