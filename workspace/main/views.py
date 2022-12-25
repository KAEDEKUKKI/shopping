from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from main.models import Product, Category
from cart.cart import Cart
from main.stock import Stock

# Create your views here.
def homePageView(request):
    all_category = Category.objects.all()
    all_products = None
    if 'categorySearch' in request.POST:
        all = request.POST.get('all')
        boxes = request.POST.getlist('boxes')
        if not all:
            all_products = Product.objects.raw('select * from main_product where main_product.category_id in (%s)' % ','.join(str(i) for i in request.POST.getlist('boxes')))
    if all_products == None:
        all_products = Product.objects.all()
    paginator = Paginator(all_products, 6)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'homepage.html', locals())

def productView(request, product_id):
    try:
        cart = Cart(request)
        product = Product.objects.raw('select * from main_product where id = %s' % product_id)[0]
        stock = Stock(product)
        if product is not None:
            if 'addToCart' in request.POST:
                quantity = request.POST['quantity']
                if stock.check(int(quantity), cart, product):
                    cart.add(product=product, quantity=int(quantity))
                else:
                    messages.warning(request, 'bought too much')
            return render(request, 'product.html', locals())
    except:
        return redirect('/')
