from typing import Optional

from fastapi import FastAPI

from apps.models import Item

app = FastAPI(
    title = 'Fast API Sample',
    description = 'Fast API description',
    version = '1.0.0',
    debug = True
)


@app.get('/')
async def get_index():
    return { 'Hello': 'World' }


@app.get('/item/{item_id}')
async def get_item(item_id: int, q: Optional[str] = None):
    return { 'item_id': item_id, 'q': q }


@app.put('/item/{item_id}')
async def put_item(item_id: int, item: Item):
    return { 'item_id': item_id, 'item_name': item.name }
