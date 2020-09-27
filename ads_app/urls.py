from django.urls import path
from django.urls import include, path
from rest_framework import routers
from ads_app import views

router = routers.DefaultRouter()
router.register(r'ads', views.UserViewSet,basename='ads')

urlpatterns = [
    path('', include(router.urls)),
]