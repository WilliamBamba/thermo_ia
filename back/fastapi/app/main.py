from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routes import weather, profile, sensor
from app.database import config as db_config, models

from app.ai import models as ai_models

models.Base.metadata.create_all(bind=db_config.engine)


app = FastAPI()

app.state.env = ai_models.Environment(23, 23, 20, [])
app.state.agent = ai_models.Agent(5, app.state.env)
app.state.word = ai_models.world
app.state.outcome = 0



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



