from fastapi import FastAPI

from app.routes import weather, profile
from app.database import config as db_config, models

models.Base.metadata.create_all(bind=db_config.engine)

def get_db():
    db = db_config.SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()
app.state.get_db = get_db



app.include_router(weather.router, prefix='/weather')
app.include_router(profile.router, prefix='/profil')


