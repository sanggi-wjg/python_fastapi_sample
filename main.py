from typing import Optional

from fastapi import FastAPI

from apps.models import Item

"""
uvicorn main:app --reload
"""

app = FastAPI(
    title = 'Fast API Sample',
    description = 'Fast API description',
    version = '1.0.0',
    debug = True
)


@app.get('/')
async def get_index():
    return { 'Hello': 'World' }


@app.get('/item/{item_id}', name = 'item_id 정보 가져오기', description = 'get_item description')
async def get_item(item_id: int, q: Optional[str] = None):
    return { 'item_id': item_id, 'q': q }


@app.put('/item/{item_id}', name = 'item_id 정보 수정')
async def put_item(item_id: int, item: Item):
    return { 'item_id': item_id, 'item_name': item.name }
