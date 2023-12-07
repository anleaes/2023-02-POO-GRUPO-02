from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'materials_used'

router = routers.DefaultRouter()
router.register('', views.Material_UsedViewSet, basename='materiais_utilizados')

urlpatterns = [
    path('', include(router.urls) )
]