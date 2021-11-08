from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi.params import Depends
from ..database import get_db
from .. import schemas, models
from passlib.context import CryptContext
from .login import AuthHandler


router = APIRouter(tags=['Fans'], prefix='/fans')

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

auth_handler = AuthHandler()


# GET
# Ejemplo de path parameter: username
@router.get('/perfil/{username}')
def profile(username: str, current_user: schemas.Fan = Depends(auth_handler.auth_wrapper)):
    return f"Esta es una pagina de usuario para el Ramarófilo {username.title()}"


@router.get('/perfil/{username}/comentarios')
# Ponemos el query parameter coment_id, agregándolo en la func pero no en la ruta.
# Para acceder a coment_id agrego ?coment_id=x a la ruta
def profile_coment(username: str, coment_id: int = None,  # El none evita el error si no se ingresa el query param
                   current_user: schemas.Fan = Depends(auth_handler.auth_wrapper)):
    return f"Página para el comentario n {coment_id} del Ramarófillo {username.title()}"


# POST
@router.post('/registro')
def create_fan(request: schemas.Fan, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(request.password)
    new_fan = models.Fan(username=request.username, email=request.email, password=hashed_password)
    db.add(new_fan)
    db.commit()
    db.refresh(new_fan)
    return new_fan
