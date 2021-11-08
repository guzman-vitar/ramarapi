from pydantic import BaseModel, Field, HttpUrl
from typing import List, Set


# Usamos pydantic para definir los schemas de datos que vamos a usar en los requests de nuestra api.
# No confundir con los models que necesita sqlalchemy para hacer las bases.

# Usuarios y login
class Fan(BaseModel):
    username: str
    email: str
    password: str


class Login(BaseModel):
    username: str
    password: str


# Productos
class Image(BaseModel):
    url: HttpUrl  # Una estructura adicional mas alla del basemodel
    name: str


class Product(BaseModel):
    name: str
    description: str
    tags: Set[str] = {}
    image: List[Image]
    # Field agrega info a estructura pydantic
    price: int = Field(
        title="Precio en USD del item",
        description="Conocer a Ramaro no tiene precio, para todo lo demas existe mastercadr",
        gt=0)

    # Schema extra proporciona datos de ejemplo.
    class Config:
        schema_extra = {
            "example": {
                "name": "Ramera",
                "description": "Una ramera de Ramaro",
                "price": 1500,
                "tags": ["vestimenta", "hogar"],
                "image": [
                    {"url": "http://www.La_vida_por_Ramaro.com",
                     "name": "Imagen Ramera_1"},
                    {"url": "http://www.La_vida_por_Ramaro.com",
                     "name": "Imagen Ramera_2"}
                ]
            }
        }
