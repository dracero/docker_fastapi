from datetime import datetime
import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Tema(BaseModel):
    description: str = Field(...)
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "description": "Este es el comienzo del tema de cinemática."
            }
        }

class Item(BaseModel): #defino el modelo de la entrada por body
    texto: str