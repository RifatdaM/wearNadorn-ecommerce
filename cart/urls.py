from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/',views.cart_summary, name='cart_summary'),
]
