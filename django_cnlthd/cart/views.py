from django.http import HttpResponseRedirect
from django.shortcuts import render
from cart.models import Cart, CartItem
from products.models import Product, SizeVariant, ColorVariant
from django.contrib import messages
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def add(value, arg):
    return value + arg


def add_to_cart(request, product_id):
    variant = request.GET.get('variant')
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get_or_create(
        user=request.user,
        is_paid=False
    )
    cart_item = CartItem.objects.get_or_create(
        cart=cart[0],
        product=product,
        quantity=1,
        user=request.user
    )
    if cart_item[0].quantity > 0:
        cart_item[0].quantity += 1
    if variant:
        variant = request.GET.get('varient')
        size_variant = SizeVariant.objects.get(size_name=variant)
        cart_item[0].size_variation = size_variant
        color_variant = ColorVariant.objects.get(color_name=variant)
        cart_item[0].color_variation = color_variant
    cart_item[0].save()
    cart_item_list = CartItem.objects.filter(
        user=request.user,
        cart=cart[0]
    )
    context = {
        'cart': cart,
        'cart_items': cart_item_list
    }
    return render(request, 'cart/cart.html', context=context)

def add_quantity_of_product(request, cart_item_id, product_id):
    product = Product.objects.get(
        id=product_id
    )
    cart_item = CartItem.objects.get(
        id=cart_item_id,
        product=product,
        user=request.user
    )
    cart_item.quantity+=1
    cart_item.save()
    cart = Cart.objects.get_or_create(
        user=request.user,
        is_paid=False
    )
    cart_item_list = CartItem.objects.filter(
        user=request.user,
        cart=cart[0]
    )
    context = {
        'cart': cart,
        'cart_items': cart_item_list
    }
    return render(request, 'cart/cart.html', context=context)

def remove_quantity_of_product(request, cart_item_id, product_id):
    product = Product.objects.get(
        id=product_id
    )
    cart_item = CartItem.objects.get(
        id=cart_item_id,
        product=product,
        user=request.user
    )
    if cart_item.quantity == 0:
        cart_item.delete()
    if cart_item:
        cart_item.quantity-=1
        cart_item.save()
    cart = Cart.objects.get_or_create(
        user=request.user,
        is_paid=False
    )
    cart_item_list = CartItem.objects.filter(
        user=request.user,
        cart=cart[0]
    )
    context = {
        'cart': cart,
        'cart_items': cart_item_list
    }
    return render(request, 'cart/cart.html', context=context)
  

def remove_cart(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(
            id=cart_item_id,
            user=request.user
        )
        cart_item.delete()

        cart = Cart.objects.get_or_create(
            user=request.user,
            is_paid=False
        )
        cart_items_list = CartItem.objects.filter(
            user=request.user,
            cart=cart[0]
        )
        context = {
            'cart': cart,
            'cart_items': cart_items_list
        }
    except Exception as e:
        print(e)
    return render(request, 'cart/cart.html', context=context)

def cart(request):
    try:
        cart = Cart.objects.get_or_create(
            user=request.user,
            is_paid=False
        )
        cart_items_list = CartItem.objects.filter(
            user=request.user,
            cart=cart[0]
        )
        context = {
            'cart': cart,
            'cart_items': cart_items_list,
            'total_price': cart[0].get_cart_total()
        }
        return render(request, 'cart/cart.html', context=context)
    except Cart.DoesNotExist:
        return render(request, 'cart/cart.html')
