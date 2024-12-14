from pydantic import BaseModel
from typing import Dict

class ImageData(BaseModel):
    image: str
    dict_of_vars: Dict