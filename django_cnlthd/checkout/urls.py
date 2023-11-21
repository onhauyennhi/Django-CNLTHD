from django.urls import path
from checkout.views import place_order, checkout, checkout_success

app_name = "checkout"

urlpatterns = [
    path('', checkout, name='checkout'),
    path('place_order/', place_order, name='place_order'),
    path('success/', checkout_success, name="checkout_success")
]
