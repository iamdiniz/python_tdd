from uuid import UUID
from store.schemas.product import ProductOut
from store.usecases.product import product_usecase


async def test_usecases_should_return_sucess(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Xbox"


async def test_usecases_get_should_return_sucess(product_id):
    result = await product_usecase.get(id=product_id)

    assert isinstance(result, ProductOut)
    assert result.name == "Xbox"


async def test_usecases_get_should_not_found():
    await product_usecase.get(id=UUID("64e6b7c46a4e4f1a8d2d3b9c"))
