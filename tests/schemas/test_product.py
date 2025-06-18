from pydantic import ValidationError
import pytest
from uuid import UUID
from store.schemas.product import ProductIn
from tests.schemas.factories import product_data


def test_schemas_return_sucess():
    data = product_data()
    product = ProductIn.model_validate(
        data
    )  # pode passar usando o model validate tambem

    assert product.name == "Xbox"
    assert isinstance(product.id, UUID)


def test_schemas_return_raise():
    data = {"name": "Xbox", "quantity": 10, "price": 2.000}

    with pytest.raises(ValidationError) as e:
        ProductIn.model_validate(data)

    assert e.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Xbox", "quantity": 10, "price": 2.0},
        "url": "https://errors.pydantic.dev/2.11/v/missing",
    }
