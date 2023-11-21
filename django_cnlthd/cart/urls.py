from django.urls import path
from cart.views import add_to_cart, remove_cart, cart, add_quantity_of_product, remove_quantity_of_product

app_name = "cart"

urlpatterns = [
    path('', cart, name='cart'),
    path('add_cart/<int:product_id>/', add_to_cart, name='add_cart'),
    path('remove_cart/<int:cart_item_id>/', remove_cart, name='remove_cart'),
    path('add_quantity_cart/<int:cart_item_id>/<int:product_id>/', add_quantity_of_product, name="add_quantity_cart"),
    path('remove_quantity_cart/<int:cart_item_id>/<int:product_id>/', remove_quantity_of_product, name="remove_quantity_cart")
    # path('remove_cart_item/<int:product_id>/<int:cart_item_id>/',remove_cart_item, name='remove_cart_item'),
    # path('checkout/',checkout, name='checkout')
]
