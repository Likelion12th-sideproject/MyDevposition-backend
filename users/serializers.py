from rest_framework.serializers import ModelSerializer

from .models import User

class UserGradeSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['grade']