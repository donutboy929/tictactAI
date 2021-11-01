import pytest
import sys
sys.path.insert(0, '/Users/danielng/projects/store_application/src')  # adding src to path
from store import *
from product import *

store = None

@pytest.fixture(autouse=True)
def before_test():
    global store
    store = Store()

def test_can_add_product():
    store.add_product(Product(1))
    assert len(store.view_products()) == 1

def test_can_remove_product():
    product = Product(1)
    store.add_product(product)
    store.remove_product(product)
    assert len(store.view_products()) == 0


def test_throws_exception_if_removing_product_absent_in_store():
    with pytest.raises(Exception) as err:
        store.remove_product(Product(1))
    # assert str(err) == "Product not in store"

def test_can_view_product():
    store.add_product(Product(1))
    store.add_product(Product(2))
    store.add_product(Product(3))
    assert len(store.view_products()) == 3

def test_cannot_add_same_product_twice():
    store.add_product(Product(1))
    store.add_product(Product(1))
    assert len(store.view_products()) == 1

def test_given_a_new_store_then_there_are_no_products():
    assert len(store.view_products()) == 0

def test_can_add_first_customer():
    store.add_new_customer()
    assert len(store.customers) == 1

def test_can_get_first_customer():
    store.add_new_customer()
    assert not store.get_first_customer() == None

def test_can_get_product_by_id():
    product = Product(1)
    store.add_product(product)
    assert store.get_product_with_id(1) == product
