from typing import List
import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import models
from app import schemas
from app.database import crud, config

router = APIRouter()

#### TODO: mettre les bonnnes HTTP status

@router.get('/', response_model=List[schemas.SensorData])
def get_sensor_data(db: Session = Depends(config.get_db)):
    return crud.get_all(db, models.SensorData)


@router.post('/', response_model=schemas.SensorData)
def create_sensor_data(sensor_data: schemas.CreateSensorData, db: Session = Depends(config.get_db)):
    return crud.create_model(db, models.SensorData, sensor_data) 
