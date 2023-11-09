# Order
class Order:
    def _init_(self, total_price, status, client):
        self.total_price = total_price
        self.status = status
        self.client = client