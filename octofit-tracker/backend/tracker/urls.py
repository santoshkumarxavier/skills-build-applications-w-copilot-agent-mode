from django.urls import path
from django.http import JsonResponse


def api_root(request):
    return JsonResponse({'message': 'OctoFit Tracker API root'})


urlpatterns = [
    path('', api_root, name='api-root'),
]
