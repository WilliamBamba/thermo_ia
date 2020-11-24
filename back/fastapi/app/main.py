from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routes import weather, profile, sensor
from app.database import config as db_config, models

from app.ai import models as ai_models

models.Base.metadata.create_all(bind=db_config.engine)


app = FastAPI()

# app.state.smartAgent = aiModels.SmartAgent()
# app.state.smartEnv = aiModels.Environment(Tint=20, Tvoulue=23, Text=20, agenda=['8:00-11:45', '14:00-18:30'])
# app.state.action = 2 # don't do anything
# app.state.lastOutcome = 0


origins = [
    "http://localhost",
    "http://localhost:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(weather.router, prefix='/weather')
app.include_router(profile.router, prefix='/profiles')
app.include_router(sensor.router, prefix='/sensors')

app.mount("/", StaticFiles(directory="app/static", html=True), name="static")



