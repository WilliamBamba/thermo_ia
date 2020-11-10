from app.database.models import Agenda, Profile
from pydantic import BaseModel
from typing import List, Optional



class CreateProfile(BaseModel):
    name: str


class Profile(CreateProfile):
    id: int
    agenda_id: Optional[int]
    option_id: Optional[int]

    class Config:
        orm_mode = True


# TODO: à supprimer
class CreateDay(BaseModel):
    day: str
    absent_hours: str# formate "8:30-12,14-18" 
    agenda_id: int

# TODO: à supprimer
class Day(CreateDay):
    id: int

    class Config:
        orm_mode = True

# TODO: à supprimer
class CreateAgenda(BaseModel):
    name: str

# TODO: à supprimer
class Agenda(CreateAgenda):

    id: int
    profiles: List[Profile]
    days: List[Day]

    class Config:
        orm_mode = True