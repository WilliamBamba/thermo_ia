from fastapi import FastAPI

from app.routes import weather, profile
from app.database import config as db_config, models

models.Base.metadata.create_all(bind=db_config.engine)



app = FastAPI()


app.include_router(weather.router, prefix='/weather')
app.include_router(profile.router, prefix='/profiles')


