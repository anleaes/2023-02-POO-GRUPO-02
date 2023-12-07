from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'contribuitors'

router = routers.DefaultRouter()
router.register('', views.ContribuitorViewSet, basename='contribuintes')

urlpatterns = [
    path('', include(router.urls) )
]