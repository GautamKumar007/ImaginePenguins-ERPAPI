from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import RegistrationSerializer
import requests
from . models import User
from rest_framework.authtoken.models import Token

# Create your views here.   

def index(request):
    return HttpResponse('<h1 style="color:green;">Welcome to ERPAPI</h1><h3>To use this UserApi:</h3><p>Use <span style="color:blue;">http://127.0.0.1:8000/api/erpapi/v1/user/register</span> to register.<br>Use <span style="color:blue;">http://127.0.0.1:8000/api/erpapi/v1/user/login</span> to get the token as responce.</p>')

class Registration(APIView):

    def get(self, request):
        item = User.objects.all()
        serializer = RegistrationSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.POST)
        data = {}
        if serializer.is_valid():
            register = serializer.save()
            data['response'] = 'Successfully registerd as User'
            data['username'] = register.username
            data['email'] = register.email
            token = Token.objects.get(user=register).key
            data['token'] = token
            print(data)
        else:
            print('error\n')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data)

