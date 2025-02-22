from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from .models import PolygonData,MultiPointData
from .serializers import MultiPolygonSerializer,MultiPointSerializer
from django.shortcuts import get_object_or_404

class MultiPolygonViewSet(ModelViewSet):
    queryset = PolygonData.objects.all()
    serializer_class = MultiPolygonSerializer

    def list(self, request, *args, **kwargs):
        queryset=PolygonData.objects.all()
        res=MultiPolygonSerializer(queryset,many=True).data
        return Response(res)
    
    def create(self, request, *args, **kwargs):
        try:
            ser=MultiPolygonSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": f"Invalid GeoJSON format: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    
class MultiPointViewset(ModelViewSet):
    queryset=MultiPointData.objects.all()
    serializer_class=MultiPointSerializer

    def list(self, request, *args, **kwargs):
        queryset=MultiPointData.objects.all()
        res=MultiPointSerializer(queryset,many=True).data
        return Response(res)
    
    def create(self, request, *args, **kwargs):
        try:
            ser=MultiPointSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": f"Invalid GeoJSON format: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        

class MultiPolygonRetrieveUpdateViewset(ModelViewSet):
    serializer_class=MultiPolygonSerializer
    queryset=PolygonData.objects.all()
    def retrieve(self, request,pk, *args, **kwargs):
        obj=get_object_or_404(PolygonData, pk=pk)
        res=MultiPolygonSerializer(obj).data
        return Response(res)
    
    def update(self, request, *args, **kwargs):
        try:
            obj=get_object_or_404(PolygonData, pk=kwargs['pk'])
            ser=MultiPolygonSerializer(obj, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"Invalid GeoJSON format: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

class MultiPointRetrieveUpdateViewset(ModelViewSet):
    serializer_class=MultiPointSerializer
    queryset=MultiPointData.objects.all()
    def retrieve(self, request, pk, *args, **kwargs):
        obj=get_object_or_404(MultiPointData, pk=pk)
        res=MultiPointSerializer(obj).data
        return Response(res)
    
    def update(self, request, *args, **kwargs):
        try:
            obj=get_object_or_404(MultiPointData, pk=kwargs['pk'])
            ser=MultiPointSerializer(obj, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"Invalid GeoJSON format: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
     