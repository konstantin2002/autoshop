from django.db import models

class Car(models.Model):

    brand = models.CharField(max_length=30)
    mod = models.CharField(max_length=30, default='not_defined')
    engine_type = models.CharField(max_length=30)
    year_made = models.CharField(max_length=30)
    gear_box = models.CharField(max_length=30)

class CarSearch(models.Model):
    
    brand = models.CharField(max_length=30)
    mod = models.CharField(max_length=30)
    engine_type = models.CharField(max_length=30)
    year_made = models.CharField(max_length=30)