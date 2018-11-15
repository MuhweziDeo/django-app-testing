from mixer.backend.django import mixer
import pytest
from products.models import Product

@pytest.mark.django_db
class TestModels:

    def test_product_is_in_stock(self):
        product = mixer.blend(Product, quantity=1)
        assert product.is_in_stock() == True

    def test_product_is_not_stock(self):
    	product=mixer.blend(Product,quantity=0)
    	assert product.is_in_stock() == False