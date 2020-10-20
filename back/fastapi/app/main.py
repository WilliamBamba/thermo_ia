from typing import Optional
from fastapi import FastAPI

from .routes import weather

app = FastAPI()

app.include_router(weather.router, prefix='/weather')


@app.get('/')
async def read_root():
    return {'Hello': 'World'}


@app.get('/items/{item_id}')
async def read_item(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id, 'q': q}
