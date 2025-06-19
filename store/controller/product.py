from typing import List
from fastapi import APIRouter, status, Body, Depends, Path, HTTPException
from pydantic import UUID4
from store.core.exceptions import NotFoundException
from store.schemas.product import ProductIn, ProductOut, ProductUpdate
from store.usecases.product import Productusecase

router = APIRouter(tags=["products"])

@router.post(path="/", status_code=status.HTTP_201_CREATED)
async def post(body: ProductIn = Body(...), usecase: Productusecase = Depends()) -> ProductOut:
    return await usecase.create(body=body)


@router.get(path="/{id}", status_code=status.HTTP_200_CREATED)
async def get(id: UUID4 = Path(alias="id"), usecase: Productusecase = Depends()) -> ProductOut:
    try:
        return await usecase.get(id=id)
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e.message))


@router.get(path="/", status_code=status.HTTP_200_OK)
async def query(usecase: Productusecase = Depends()) -> List[ProductOut]:
    return await usecase.query()


@router.patch(path="/{id}", status_code=status.HTTP_200_CREATED)
async def patch(id: UUID4 = Path(alias="id"), body: ProductUpdate = Body(...) , usecase: Productusecase = Depends()) -> ProductOut:
    return await usecase.update(id=id, body=body)


@router.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: UUID4 = Path(alias="id"), usecase: Productusecase = Depends()) -> None:
    try:
        await usecase.delete(id=id)
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e.message))