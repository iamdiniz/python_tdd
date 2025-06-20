from datetime import datetime
from decimal import Decimal
from bson import Decimal128
from typing import Annotated, Optional, AfterValidator
from pydantic import Field, BaseModel, UUID4, model_validator
from store.schemas.base import BaseSchemaMixin, OutMixin


class ProductBase(BaseModel):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: Decimal = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn, OutMixin):
    ...
   

def convert_decimal128(v):
    return Decimal128(str(v))

Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal128)]

class ProductUpdate(BaseSchemaMixin):
    quantity: Optional[int] = Field(None, description="Product quantity")
    price: Optional[Decimal] = Field(None, description="Product price")
    status: Optional[bool] = Field(None, description="Product status")
    

class ProductUpdateOut(ProductOut):
    ...