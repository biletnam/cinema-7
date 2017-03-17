from django.shortcuts import render, HttpResponse
from cinema.account.models import User
from django.contrib.auth import authenticate
import json

def auth_user(request, user_json='{"email": "test@test.com", "password": "12345678"}'):
    user_info = json.loads(user_json)
    user = authenticate(email=user_info["email"], password=user_info["password"])
    if user is not None:
        return HttpResponse('ok')
    else:
        return HttpResponse('not ok')

def create_user(request, user_json='{"email": "test@test.com", "password": "12345678", "phone = "123"}'):
    user_info = json.loads(user_json)
    user_phone = int(user_info["phone"])
    if user_phone is not None:
        user = User.objects.create_user(email=user_info["email"], password=user_info["password"], phone=user_phone)
        return HttpResponse("user "+user.email+" created")
    else:
        return HttpResponse("not ok")

def account_info(request, id=0):
    return HttpResponse("account page dummy")
