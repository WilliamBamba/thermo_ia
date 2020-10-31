from app.database.models import Profile
from pydantic import BaseModel


class CreateProfile(BaseModel):
    name: str

class Profile(CreateProfile):
    id: int

    class Config:
        orm_mode = True