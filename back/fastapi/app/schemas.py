from pydantic import BaseModel
from typing import List, Optional



class CreateProfile(BaseModel):
    name: str


class UpdateProfile(CreateProfile):

    time_table: Optional[str] # (8-11:45) (12:45-17)
    url_agenda: Optional[str] # valide url pointing to a .ics celander
    option_id: Optional[int]


class Profile(UpdateProfile):
    id: int

    class Config:
        orm_mode = True


class CreateSensorData(BaseModel):

    temperature: int

