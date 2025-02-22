# Create your models here.
from django.contrib.gis.db import models

class PolygonData(models.Model):
    name = models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    population = models.FloatField()
    polygons = models.MultiPolygonField()  

    def __str__(self):
        return self.name


class MultiPointData(models.Model):
    name = models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    points = models.MultiPointField()  

    def __str__(self):
        return self.name
