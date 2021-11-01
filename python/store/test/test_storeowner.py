import pytest
import sys
sys.path.insert(0, '/Users/danielng/projects/store_application/src')  # adding src to path
from storeowner import *
from store import *
from product import *

store = None
storeowner = None

@pytest.fixture(autouse=True)
def before_test():
    global store, storeowner
    store = Store()
    store.add_new_customer()
    storeowner = StoreOwner(store)

def test_can_get_total_price_of_a_basket():
    # store.add_new_customer()
    customer = storeowner.get_first_customer()
    customer.get_basket().add_product(Product(1))
    customer.get_basket().add_product(Product(1))
    customer.get_basket().add_product(Product(1))
    assert storeowner.get_total_price_of_basket_of_first_customer() == 3

def test_can_view_first_customer():
    assert not storeowner.get_first_customer() == None
