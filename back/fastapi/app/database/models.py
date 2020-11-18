from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.database.config import Base



class Profile(Base):

    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    city = Column(String)
    wtemp = Column(Integer, default=23)
    time_table = Column(String, nullable=True) # "[8-11:45],[12:45-17]"
    url_agenda = Column(String, nullable=True) # valide url pointing to a .ics celander
    option_id = Column(Integer, ForeignKey('option.id'), nullable=True)


    # input: (8-9:45) (10-11:45) (12:45-17)
    # output: (8-11:45) (12:45-17)
    def parse_agenda():
        pass


    def refresh_agenda(self):
        pass


class Option(Base):

    __tablename__ = "option"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)


class SensorData(Base):

    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=True)
