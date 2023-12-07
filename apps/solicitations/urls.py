from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'solicitations'

router = routers.DefaultRouter()
router.register('', views.SolicitationViewSet, basename='solicitacoes')

urlpatterns = [
    path('', include(router.urls) )
]