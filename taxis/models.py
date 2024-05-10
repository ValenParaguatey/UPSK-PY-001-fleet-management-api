from django.db import models # type: ignore

class Taxi(models.Model):
    id = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=255)

#specificar metadatos del modelo
class Meta: 
    db_table = "taxis"