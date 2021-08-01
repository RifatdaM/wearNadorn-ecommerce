import cart
from django.http import response
from django.shortcuts import get_object_or_404, render
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    cart = Cart(request)
    return render(request, 'store/cart/summary.html', {'cart': cart })

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=product_qty)
        
        totalqty = cart.__len__()
        response = JsonResponse({'qty':totalqty})
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        cart.delete(product=product_id)
        response = JsonResponse({'Success': True})
        return response 