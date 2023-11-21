from django.shortcuts import render
from products.models import Product
from cart.models import Cart


def index(request):
    user = request.user
    context = {
        'products' : Product.objects.all(), 
        'user': user,
    }
    return render(request , 'home/index.html' , context)
