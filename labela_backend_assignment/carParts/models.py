from django.db import models


class CarPart(models.Model):
    part_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.PositiveIntegerField()

    def __str__(self):
        return self.part_name
    
