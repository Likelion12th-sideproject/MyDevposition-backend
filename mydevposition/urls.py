from django.contrib import admin
from django.urls import path

from rest_framework import routers

from users.views import UserModelViewSet, post_grade

router = routers.DefaultRouter()
router.register('users', UserModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/{int:user_id}/grade', post_grade),
]