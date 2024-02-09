from rest_framework.serializers import ModelSerializer

from .models import User

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        fields = ['id', 'grade', 'result']