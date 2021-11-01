from store import *

class StoreOwner():
    def __init__(self, store=Store()):
        self.store = store

    def get_store(self):
        return self.store

    def get_first_customer(self):
        return self.store.get_first_customer()

    def get_total_price_of_basket_of_first_customer(self):
        return self.store.get_first_customer().get_basket().get_total_price()
