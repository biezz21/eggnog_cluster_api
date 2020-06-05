from django.urls import path, include
from rest_framework import routers
from .views import CountarrayViewset, DescViewset

router = routers.DefaultRouter()
router.register('countarray', CountarrayViewset, basename='Count Array')
router.register('desc', DescViewset, basename='Description')
urlpatterns = [
    path('', include(router.urls)),
]
