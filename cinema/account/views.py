from django.shortcuts import render, HttpResponse
from cinema.account.models import UserManager, User
from django.contrib.auth import authenticate
import json

def auth_user(request, user_json='{"email": "test@test.com", "password": "12345678"}'):
    user_info = json.loads(user_json)
    user = authenticate()
    return HttpResponse('ok')

def create_user(request, user_json='{"email": "test@test.com", "password": "12345678"}'):
    user_info = json.loads(user_json)
    user = User.objects.create_user(email=user_info["email"], password=user_info["password"])
    return HttpResponse("user"+user.email+"created")