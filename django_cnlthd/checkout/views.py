from datetime import datetime
from django.shortcuts import redirect, render

from cart.models import Cart, CartItem
from checkout.models import Order, OrderProduct
from products.models import Product

def checkout(request):
    current_user = request.user

    cart = Cart.objects.get_or_create(
        user=current_user,
        is_paid=False
    )
    cart_items = CartItem.objects.filter(
        user=current_user,
        cart=cart[0]
    )
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('index')
    grand_total = 0
    total=0
    quantity=0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    grand_total = total 
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total': total,
        'grand_total': grand_total,
    }
    return render(request, 'checkout/checkout.html', context)


def place_order(request):
    current_user = request.user

    cart = Cart.objects.get_or_create(
        user=current_user,
        is_paid=False
    )
    cart_items = CartItem.objects.filter(
        user=current_user,
        cart=cart[0]
    )
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('index')

    grand_total = 0
    total=0
    quantity=0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    grand_total = total 

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address_line_1 = request.POST.get('address_line_1')
        address_line_2 = request.POST.get('address_line_2')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        order_note = request.POST.get('order_note')
        order_total = grand_total
        new_order = Order(
            user=current_user,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            country=country,
            state=state,
            order_note=order_note,
            city=city,
            order_total=order_total
        )
        new_order.save()
        order_number = 'ODC' + str(new_order.id)
        new_order.order_number = order_number
        new_order.save()

        order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
        for item in cart_items:
            order_product = OrderProduct()
            order_product.order_id = order.id
            order_product.user_id = request.user.id
            order_product.product_id = item.product_id
            order_product.quantity = item.quantity
            order_product.product_price = item.product.price
            order_product.ordered = True
            order_product.save()

            cart_item = CartItem.objects.get(id=item.id)
            order_product = OrderProduct.objects.get(id=order_product.id)
            order_product.save()

        ordered_products = OrderProduct.objects.filter(order_id=order.id)
        subtotal = 0
        for i in ordered_products:
            subtotal += i.product_price * i.quantity

        context = {
            'order': order,
            'ordered_products': ordered_products,
            'order_number': order.order_number,
            'subtotal': subtotal,
        }
        cart[0].is_paid = True
        cart[0].save()
        cart_items.delete()
        return render(request, 'checkout/success.html', context)
    else:
        return redirect('checkout')
    

def checkout_success(request):
    return render(request, 'checkout/success.html')
