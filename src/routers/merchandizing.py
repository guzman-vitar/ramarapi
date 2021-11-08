from fastapi import APIRouter, Response, HTTPException
from sqlalchemy.orm import Session
from fastapi.params import Depends
from .login import AuthHandler
from ..database import get_db
from .. import schemas, models


router = APIRouter(tags=['Merchandizing'], prefix='/productos')

auth_handler = AuthHandler()


# GET
@router.get('/')
def products(db: Session = Depends(get_db), current_user: schemas.Fan = Depends(auth_handler.auth_wrapper)):
    products = db.query(models.Product).all()
    return products


@router.get('/{id}')
def product(id, response: Response, db: Session = Depends(get_db),
            current_user: schemas.Fan = Depends(auth_handler.auth_wrapper)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    return product


# POST
@router.post('/')
def add(request: schemas.Product, current_user: schemas.Fan = Depends(auth_handler.auth_wrapper),
        db: Session = Depends(get_db)):
    new_product = models.Product(name=request.name,
                                 description=request.description,
                                 tags=request.tags,
                                 image=request.image,
                                 price=request.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request


# DELETE
@router.delete('/{id}')
def delete(id, db: Session = Depends(get_db), current_user: schemas.Fan = Depends(auth_handler.auth_wrapper)):
    db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
    db.commit()
    return {'Product deleted'}


# PUT
@router.put('/{id}')
def update(id, request: schemas.Product, db: Session = Depends(get_db),
           current_user: schemas.Fan = Depends(auth_handler.auth_wrapper)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        pass
    product.update(request.dict)
    db.commit()
    return {'Product succesfully updated'}
