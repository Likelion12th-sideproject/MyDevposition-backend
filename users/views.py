from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import HttpResponse

from .models import User
from .serializers import UserGradeSerializer

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserGradeSerializer

@api_view(['POST'])
def post_grade(request, user_id):
    if request.method == 'POST':
        serializer = UserGradeSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        return HttpResponse(status=status.HTTP_200_OK)