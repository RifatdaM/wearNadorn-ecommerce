from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/',views.cart_summary, name='cart_summary'),
    path('add/',views.cart_add, name='cart_add'),
    path('delete/',views.cart_delete, name='cart_delete'),
]
