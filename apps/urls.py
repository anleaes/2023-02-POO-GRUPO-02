from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'locations'

router = routers.DefaultRouter()
router.register('', views.LocationViewSet, basename='localizacoes')

urlpatterns = [
    path('', include(router.urls) )
]