from fastapi import APIRouter, Request

from app import schemas
from app.database import models, crud

router = APIRouter()


@router.post('/', response_model=models.Profil)
def create_profil(user: schemas.CreateProfil, request: Request):
    db = request.app.state.get_db()
    return crud.create_user(db, user)

