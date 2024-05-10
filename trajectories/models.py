from django.db import models
from taxis.models import Taxi

# Create your models here.
class Trajectories(models.Model):
    id = models.AutoField(primary_key=True)
    taxi = models.ForeignKey(Taxi, on_delete =models.CASCADE)
    date =  models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class Meta: 
    db_table = "trajectories"