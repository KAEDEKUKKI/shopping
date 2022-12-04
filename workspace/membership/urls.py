from django.urls import path
from .views import sign_up, sign_in, sign_out

urlpatterns = [
    path('register', sign_up),
    path('login', sign_in),
    path('logout', sign_out),
]
