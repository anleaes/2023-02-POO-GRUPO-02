from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'supervisors'

router = routers.DefaultRouter()
router.register('', views.SupervisorViewSet, basename='supervisores')

urlpatterns = [
    path('', include(router.urls) )
]