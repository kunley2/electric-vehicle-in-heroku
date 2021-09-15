from django.db import models


# Create your models here.
class LinearModel(models.Model):
    vehicle_name = models.CharField(max_length=200)
    battery = models.FloatField()
    acceleration = models.FloatField()
    top_speed = models.FloatField()
    distance = models.IntegerField()
    efficiency = models.FloatField()
    fast_charge = models.FloatField()
    price_usd = models.FloatField()

    def __str__(self):
        return self.vehicle_name
