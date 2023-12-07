from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'tasks'

router = routers.DefaultRouter()
router.register('', views.TaskViewSet, basename='servicos')

urlpatterns = [
    path('', include(router.urls) )
]