from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register('list', views.CarViewSet)
router.register('brand', views.BrandViewSet)
router.register('review', views.ReviewViewSet, basename='review')
urlpatterns = [
    path('', include(router.urls))
]
