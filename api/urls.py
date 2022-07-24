from django.urls import path, re_path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path('authenticate/', views.CustomObtainAuthToken.as_view())
]