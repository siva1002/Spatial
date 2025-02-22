from django.contrib import admin
from geo.models import PolygonData,MultiPointData

# Register your models here.


@admin.register(PolygonData)
class PolygonDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'polygons')

@admin.register(MultiPointData)
class MultiPointDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'points')