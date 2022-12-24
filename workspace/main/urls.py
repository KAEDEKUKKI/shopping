from django.urls import path
from .views import homePageView, productView

urlpatterns = [
    path('', homePageView),
    path('product/<slug:product_id>', productView),
]
