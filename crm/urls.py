from django.urls import path, include
from rest_framework.routers import DefaultRouter
from crm.views import CRMAPI, GetForecast

router = DefaultRouter()
router.register('crm', CRMAPI, 'crm')

urlpatterns = [
    path('', include(router.urls)),
    path('forecast/', GetForecast.as_view())
]