from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'entities'

router = routers.DefaultRouter()
router.register('', views.EntityViewSet, basename='Orgaos')

urlpatterns = [
    path('', include(router.urls) )
]