from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'materials'

router = routers.DefaultRouter()
router.register('', views.MaterialViewSet, basename='materiais')

urlpatterns = [
    path('', include(router.urls) )
]