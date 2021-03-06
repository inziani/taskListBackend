"""taskList_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
    TokenRefreshView,)
from django.views.decorators.csrf import csrf_exempt


class TaskListDefaultRouter(routers.DefaultRouter):
    def extend(self, router):
        self.registry.extend(router.registry)

router = TaskListDefaultRouter()
from users.urls import router as users_router
router.extend(users_router)
from tasks.urls import router as tasks_router
router.extend(tasks_router)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'), csrf_exempt('api-auth'), ),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', include(router.urls)),
]
