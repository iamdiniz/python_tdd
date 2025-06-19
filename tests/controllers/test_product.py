from typing import List
from tests.factories import product_data
from fastapi import status
import pytest


async def test_controller_create_should_return_sucess(client, products_url):
    response = await client.post(products_url, json=product_data())
    
    content = response.json()
    
    assert response.status_code == status.HTTP_201_CREATED
    assert content["name"] == product_data()["name"]
    

async def test_controller_get_should_return_sucess(client, products_url, product_inserted):
    response = await client.get(f"{products_url}/{product_inserted.id}")
    
    content = response.json()
    
    assert response.status_code == status.HTTP_201_CREATED
    assert content["id"] == str(product_inserted.id)


async def test_controller_get_should_return_not_found(client, products_url):
    response = await client.get(f"{products_url}a4c8b9d3e6f127ab34cd9e01")
    
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == "Product not found with filter: a4c8b9d3e6f127ab34cd9e01"
    

@pytest.mark.usefixtures("product_inserted")
async def test_controller_query_should_return_sucess(client, products_url, product_inserted):
    response = await client.get(products_url)
    
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), List)
    assert len(response.json()) > 1
    

async def test_controller_patch_should_return_sucess(client, products_url, product_inserted):
    response = await client.patch(f"{products_url}/{product_inserted.id}", json={"quantity": 40})
    
    content = response.json()
    
    assert response.status_code == status.HTTP_200_OK
    assert content["quantity"] == 40
    
    
async def test_controller_delete_should_return_no_content(client, products_url, product_inserted):
    response = await client.delete(f"{products_url}/{product_inserted.id}")
    
    assert response.status_code == status.HTTP_204_NO_CONTENT


async def test_controller_delete_should_return_not_found(client, products_url):
    response = await client.delete(f"{products_url}a4c8b9d3e6f127ab34cd9e01")
    
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == "Product not found with filter: a4c8b9d3e6f127ab34cd9e01"