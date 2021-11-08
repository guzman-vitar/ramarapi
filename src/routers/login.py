import jwt
from fastapi import APIRouter, HTTPException, Security, Depends, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from ..schemas import Login
from ..database import get_db
from .. import models


router = APIRouter(tags=['Login'], prefix='/login')


class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = 'SECRET'

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def encode_token(self, user_id):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=5),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm='HS256'
        )

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Signature has expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid token')

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)


auth_handler = AuthHandler()


@router.post('/login')
def login(auth_details: Login, db: Session = Depends(get_db)):
    fan = db.query(models.Fan).filter(models.Fan.username == auth_details.username).first()

    if not fan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Fan no encontrado/ fan inválido')
    if not auth_handler.verify_password(auth_details.password, fan.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contraseña inválida')

    token = auth_handler.encode_token(fan.username)

    return {'token': token}
