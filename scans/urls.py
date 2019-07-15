from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'scans'

router = routers.DefaultRouter()
router.register('scans', views.ScanViewSet, base_name='scans')

urlpatterns = [
    path('', include(router.urls)),
]