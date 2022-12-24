from django.urls import path
from cart.views import cartPageView, checkoutView

urlpatterns = [
    path('', cartPageView),
    path('checkout/', checkoutView),
]
