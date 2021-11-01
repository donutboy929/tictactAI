import pytest
import sys
sys.path.insert(0, '/Users/danielng/projects/store_application/src')  # adding src to path
from customer import *
from basket import *
from product import *

customer = None

@pytest.fixture(autouse=True)
def before_test():
    global customer
    customer = Customer()

def test_can_add_product_to_basket():
    product = Product(1)
    customer.get_basket().add_product(product)
    assert product in customer.get_basket().view_products_in_basket()

def test_can_remove_a_product_from_basket():
    product = Product(1)
    customer.get_basket().add_product(product)
    customer.get_basket().remove_product(product)
    assert not product in customer.get_basket().view_products_in_basket()

def test_can_view_products_in_basket():
    products = {Product(1,"A"), Product(1,"B"), Product(1,"C")}
    for item in products:
        customer.get_basket().add_product(item)
    basket = customer.get_basket().view_products_in_basket()
    assert products == basket

def test_cannot_add_product_to_basket_with_same_id():
    pass