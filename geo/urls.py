from django.urls import path,reverse
from geo.views import (MultiPolygonViewSet,MultiPointViewset,
                       MultiPolygonRetrieveUpdateViewset,MultiPointRetrieveUpdateViewset)

urlpatterns=[
    path('polygons',MultiPolygonViewSet.as_view(
        {'get': 'list',
        'post': 'create',

    })),
    path('points',MultiPointViewset.as_view(
        {'get': 'list',
        'post': 'create'}
    )),
    path('polygons/<int:pk>',MultiPolygonRetrieveUpdateViewset.as_view(
        {'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'}
    )),
    path('points/<int:pk>',MultiPointRetrieveUpdateViewset.as_view(
        {'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'}
    ))
]