from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ratings'

router = routers.DefaultRouter()
router.register('', views.RatingViewSet, basename='avaliacoes')

urlpatterns = [
    path('', include(router.urls) )
]