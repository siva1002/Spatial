from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import MultiPointData,PolygonData


class MultiPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MultiPointData
        fields = ["id", "name", "points","description"]
        geo_field = "points"



class MultiPolygonSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PolygonData
        fields = ["id", "name", "polygons","city","population"]
        geo_field = "polygons"
    
    def create(self, validated_data):
        instance= PolygonData.objects.create(
            **validated_data
        )
        return instance

class MultiPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MultiPointData
        fields = ["id", "name", "points","description"]
        geo_field = "points"