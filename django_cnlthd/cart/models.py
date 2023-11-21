# Create your models here.
from auth_app.models import User
from django.db import models

from products.models import Product, SizeVariant, ColorVariant


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    date_added = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
    
    def get_cart_total(self):
        cart_items = self.cart_items.all()
        price = []
        for cart_item in cart_items:
            price.append(cart_item.product.price*cart_item.quantity)
            # if cart_item.color_variation:
            #     color_variant_price = cart_item.color_variation
            #     price.append(color_variant_price)
            # if cart_item.size_variation:
            #     size_variant_price = cart_item.size_variation
            #     price.append(size_variant_price)
        return sum(price)

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size_variation = models.ManyToManyField(SizeVariant, blank=True)
    color_variation = models.ManyToManyField(ColorVariant, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, related_name='cart_items')
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.quantity * self.product.price

    def __unicode__(self):
        return self.product
