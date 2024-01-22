from django.db import models
from users.models import User
from carParts.models import CarPart


class ShoppingCart(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    CarPartID = models.ForeignKey(CarPart, on_delete=models.CASCADE)
    #quantity = models.PositiveIntegerField()

