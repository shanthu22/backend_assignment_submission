from django.contrib import admin
from django.urls import path
from shoppingCarts.views import shoppingCart
from carParts.views import carParts  # ,tempcarParts
from products.views import HandleProductsRequest, HandleAllProductsRequest
urlpatterns = [

    # path('carParts/', carParts, name='carParts'),
    path('shoppingCart/<int:RequestedUserID>/',
         shoppingCart, name='ShoppingCart'),
    # path('product/', HandleAllProductsRequest, name='allProducts'),
    path('product/', HandleProductsRequest, name='products'),
    path('product/<int:productID>/', HandleProductsRequest, name='products')


]
