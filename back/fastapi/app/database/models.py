from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .config import Base


class Profil(Base):
    __tablename__ = "profil"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
