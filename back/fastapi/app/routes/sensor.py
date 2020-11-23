from typing import List
import ast

from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect, Request
from sqlalchemy.orm import Session

from app.database import models
from app import schemas
from app.database import crud, config

router = APIRouter()


#### TODO: mettre les bonnnes HTTP status


@router.get('/', response_model=List[schemas.SensorData])
def get_sensor_data(db: Session = Depends(config.get_db)):
    return crud.get_all(db, models.SensorData)

@router.get('/most_recent', response_model=schemas.SensorData)
def get_most_recent_sensor_data(db: Session = Depends(config.get_db)):
    return crud.get_most_recent_model(db, models.SensorData)


@router.post('/', response_model=schemas.SensorData)
def create_sensor_data(sensor_data: schemas.CreateSensorData, db: Session = Depends(config.get_db)):
    return crud.create_model(db, models.SensorData, sensor_data) 


@router.websocket('/exchange_data')
async def sensor_data_exchange(websocket: WebSocket, db: Session = Depends(config.get_db)):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            temp_dict = ast.literal_eval(data)
            sensor_data = schemas.CreateSensorData(**temp_dict)
            crud.create_model(db, models.SensorData, sensor_data) 

            await websocket.send_json(sensor_data.json())
    except WebSocketDisconnect:
        pass