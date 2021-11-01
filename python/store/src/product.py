import uuid

class Product():
    def __init__(self, id, name="unnamed", price=1):
        self.name = name
        self.id = id
        self.price = price

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_price(self):
        return self.price