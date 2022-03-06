from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter, SimpleRouter

from users import views
from users.views import UserViewSet, UserProfileViewSet

router = SimpleRouter()

router.register(r'users', views.UserViewSet)
router.register(r'userProfile', views.UserProfileViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls))
]