from typing import Optional

from pydantic.main import BaseModel


class Item(BaseModel):
    name: str
    price: int
    is_offer: Optional[bool] = False
