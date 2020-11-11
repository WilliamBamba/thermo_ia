from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.database.config import Base


class User(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String) #, unique=True)
    


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String) #, unique=True)
    option_id = Column(Integer, ForeignKey('option.id'), nullable=False)
    # agenda_url = Column(String, nullable=False)
    # absent_hours = Column(String, nullable=False) # [(debut, fin), (debut, fin)]


    def refresh_agenda(self):
        pass




class Option(Base):

    __tablename__ = "option"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)


# TODO: à supprimer
class Agenda(Base):
    __tablename__ = "agenda"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    profiles = relationship("Profile")
    days = relationship("Day")

""""

    lun: (8:30-12:30,14-18)
    mar: ()
    mer: ()
    jeu: ()
    ven: ()
    ()
    ()
    ()

"""
# TODO: à supprimer
class Day(Base):

    __tablename__ = "day"

    id = Column(Integer, primary_key=True, index=True)
    day = Column(String, nullable=True)
    absent_hours = Column(String, nullable=False) # formate "8:30-12,14-18" 
    agenda_id = Column(Integer, ForeignKey('agenda.id'), nullable=False)



class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=True)