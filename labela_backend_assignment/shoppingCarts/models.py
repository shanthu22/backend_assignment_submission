from django.db import models
from users.models import User
from products.models import Product


class ShoppingCart(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
