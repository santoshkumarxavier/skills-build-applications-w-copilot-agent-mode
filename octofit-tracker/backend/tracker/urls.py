from django.urls import path, include
from rest_framework import routers
from .views import ActivityViewSet
from django.http import JsonResponse

router = routers.DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activity')


def api_root(request):
    return JsonResponse({
        'message': 'OctoFit Tracker API root',
        'activities': request.build_absolute_uri('activities/')
    })


urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
]
