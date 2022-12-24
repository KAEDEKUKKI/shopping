from django.shortcuts import render, redirect
from cart.cart import Cart
from main.models import Product
from cart.models import Order
import hashlib, time

# Create your views here.
def cartPageView(request):
    cart = Cart(request)
    if 'rm' in request.GET:
        product = Product.objects.raw('select * from main_product where id = %s' % request.GET['rm'])[0]
        if product is not None:
            cart.remove(product)
            return redirect('/cart')
    return render(request, 'cart.html', locals())
def checkoutView(request):
    if request.user.is_anonymous:
        return redirect('/login')
    cart = Cart(request)
    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        phone = request.POST['phone']
        address = request.POST['address']
        block_string = str(request.user)+firstName+lastName+phone+address+str(time.time())
        number = hashlib.sha256(block_string.encode()).hexdigest()
        for item in cart:
            order_item = Order(number=number, user=request.user, first_name=firstName, last_name=lastName, phone=phone, address=address, product=item['product'], quantity=item['quantity'], price=item['price'])
            order_item.save()
        cart.clear()
        return redirect('/')
    return render(request, 'checkout.html', locals())
