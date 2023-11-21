from django.urls import path
from products.views import get_product

app_name="products"

urlpatterns = [
   
    path('<slug>/' , get_product , name="get_product"),
]
