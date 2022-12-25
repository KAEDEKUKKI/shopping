from cart.models import Order
import hashlib, time

class Chumon(object):
    def __init__(self, request, firstName, lastName, phone, address):
        self.user = request.user
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.address = address
        block_string = str(self.user)+self.firstName+self.lastName+self.phone+self.address+str(time.time())
        self.number = hashlib.sha256(block_string.encode()).hexdigest()
    def add(self, product, quantity, price):
        order_item = Order(number=self.number, user=self.user, first_name=self.firstName, last_name=self.lastName, phone=self.phone, address=self.address, product=product, quantity=quantity, price=price)
        order_item.save()
