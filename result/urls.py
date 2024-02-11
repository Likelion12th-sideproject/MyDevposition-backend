from django.urls import path
from .views import ResultView

urlpatterns = [
    path('users/', ResultView.as_view(), name='save_test_result'),
]
