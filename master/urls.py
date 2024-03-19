from django.urls import path, include
from rest_framework.routers import DefaultRouter
from master.views import MasterAPI

router = DefaultRouter()
router.register('master', MasterAPI, 'master')

urlpatterns = [
    path('', include(router.urls)),
]