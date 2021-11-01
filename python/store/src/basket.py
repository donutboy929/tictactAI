class Basket():
    def __init__(self):
        self.products = set()

    def add_product(self, product):
        self.products.add(product)

    def remove_product(self, product):
        self.products.remove(product)

    def view_products_in_basket(self):
        return self.products

    def get_total_price(self):
        price = 0
        for item in self.products:
            price += item.get_price()

        return price