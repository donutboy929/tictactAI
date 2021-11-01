import sys
sys.path.insert(0, '/Users/danielng/projects/store_application/src')  # adding src to path
from product import *
import pytest

product = None


@pytest.fixture(autouse=True)
def before_test():
    global product
    product = Product(1)

def test_get_name():
    assert product.get_name() == "unnamed"

def test_get_id():
    assert product.get_id() == product.id
