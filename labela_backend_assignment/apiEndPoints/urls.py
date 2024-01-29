from django.contrib import admin
from django.urls import path
from shoppingCarts.views import shoppingCart
from products.views import HandleProductsRequest, HandleAllProductsRequest

urlpatterns = [

    path('shoppingCart/<int:RequestedUserID>/',
         shoppingCart, name='ShoppingCart'),

    # To work with Products as a whole (GET)
    path('products/', HandleAllProductsRequest, name='allProducts'),

    # To work with a specific product (GET, POST, PUT, DELETE)
    path('product/<int:productID>/', HandleProductsRequest, name='product'),
    path('product/', HandleProductsRequest, name='product POST')

]
