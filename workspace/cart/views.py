from django.shortcuts import render, redirect
from cart.cart import Cart
from main.models import Product
from cart.order import Chumon

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
        order = Chumon(request, firstName=firstName, lastName=lastName, phone=phone, address=address)
        for item in cart:
            order.add(product=item['product'], quantity=item['quantity'], price=item['price'])
        cart.clear()
        return redirect('/')
    return render(request, 'checkout.html', locals())
