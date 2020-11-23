from pydantic import BaseModel
from typing import List, Optional
import datetime



class Action(BaseModel):
    action: int
    pass


class CreateProfile(BaseModel):
    name: str
    city: str
    wtemp: int


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


class SensorData(CreateSensorData):
    id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True
