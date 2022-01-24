from django.db import models

# Create your models here.

class Flower(models.Model):
    name=models.CharField(max_length=20)
    color=models.CharField(max_length=20)
    price=models.IntegerField()
    quantity=models.IntegerField()
    class Meta:
        db_table='flowers'

