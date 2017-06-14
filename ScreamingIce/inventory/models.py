from django.db import models

# Create your models here.
class IceCream(models.Model):
    name = models.CharField(max_length=256)
    flavor = models.CharField(max_length=1024)
    description = models.TextField()
    sugar_mg = models.FloatField()
    price_dollars = models.PositiveSmallIntegerField()
    has_topping = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} Ice Cream @ ${self.price_dollars}"


