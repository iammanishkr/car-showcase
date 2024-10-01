from django.db import models

# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=100)
    hoursepower=models.FloatField()
    price=models.FloatField()
    carimage=models.ImageField(upload_to='media/',null=True,blank=True)
    
