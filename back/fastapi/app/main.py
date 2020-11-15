from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import weather, profile, agenda, sensor
from app.database import config as db_config, models


models.Base.metadata.create_all(bind=db_config.engine)


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(agenda.router, prefix='/agenda')
app.include_router(weather.router, prefix='/weather')
app.include_router(profile.router, prefix='/profiles')
app.include_router(sensor.router, prefix='/sensors')


