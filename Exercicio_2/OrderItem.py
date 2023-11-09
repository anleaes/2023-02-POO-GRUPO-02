# OrderItem
class OrderItem:
    def _init_(self, quantity, unitary_price, order, product):
        self.quantity = quantity
        self.unitary_price = unitary_price
        self.order = order
        self.product = product