from cart.models import Order

class Stock(object):
    def __init__(self, product):
        self.stock = product.stock
        order = Order.objects.raw('select * from cart_order where cart_order.product_id = %s' % product.id)
        for quantity in order:
            self.stock -= quantity.quantity
    def __str__(self):
        return str(self.stock)
    def check(self, quantity, cart, product_id):
        quantity += cart.get_quantity(product_id)
        if quantity > self.stock:
            return False
        else:
            return True
