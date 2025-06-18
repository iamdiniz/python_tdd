from uuid import UUID
from store.schemas.product import ProductIn


def test_schemas_validated():
    data = {"name": "Xbox", "quantity": 10, "price": 2.000, "status": True}
    product = ProductIn(**data)

    assert product.name == "Xbox"
    assert isinstance(product.id, UUID)
