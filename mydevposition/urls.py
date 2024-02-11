from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from users.views import UserModelViewSet, post_grade

router = routers.DefaultRouter()
router.register('users', UserModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/grade', post_grade),
    path('result/', include('result.urls')),
]