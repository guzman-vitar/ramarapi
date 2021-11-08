from fastapi import APIRouter
from fastapi.params import Depends
from .. import schemas
import numpy as np
from .login import AuthHandler


router = APIRouter(tags=['Ramarosama'], prefix='/Ramaro')

auth_handler = AuthHandler()


# GET
@router.get('/Ramaro_sama/peliculas_favoritas')
def movies(current_user: schemas.Fan = Depends(auth_handler.auth_wrapper)):
    return {'lista_peliculas': ['El_quinto_elemento', 'Aladdin']}


@router.get('/amor')
def amor(current_user: schemas.Fan = Depends(auth_handler.auth_wrapper)):
    return "Cuanto amas hoy a Ramaro? Ingresá tu usuario para averiguarlo!"


@router.get('/amor/{user}')
def amorx(user: str, current_user: schemas.Fan = Depends(auth_handler.auth_wrapper)):
    if user.lower() == 'guzman':
        amor = 1811311815
    elif user.lower() == 'gonzalo':
        amor = 'infinito y mas allá'
    else:
        amor = np.random.randint(1000)
    return f"Nivel de amor que sientes hoy por Ramaro: {amor}"
