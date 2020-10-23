from app.database.models import Profile
from pydantic import BaseModel


class CreateProfil(BaseModel):
    name: str

class Profil(CreateProfil):
    id: int