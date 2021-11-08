from fastapi import FastAPI
from src.routers import Ramaro
from . import models
from .database import engine
from .routers import merchandizing, fans, login

app = FastAPI(
    title='RamarAPI',
    description='Una API para Ramarosama, un lider técnico diferente',
    terms_of_service='http://google.com',
    contact={
        "Dev name": "Guzman",
        "email": "guzvitar@lavidaporramaro.com"
    }
)

# Traemos los routers
app.include_router(Ramaro.router)
app.include_router(merchandizing.router)
app.include_router(fans.router)
app.include_router(login.router)

models.Base.metadata.create_all(engine)


@app.get('/', tags=['Main'])
def index():
    return "Bienvenidos a la api de Ramaro, un lider técnico diferente. \
Abróchense sus cinturones y prepárense para una aventura ramarnífica"
