from django.shortcuts import render, HttpResponse, redirect
from cinema.account.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
import json


def login_view(request):
    return render(request, 'login.html')

@csrf_protect
def signup_view(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'signup.html', c)

def redirect_to_self(request):
    if request.user is not None:
        return redirect("./"+str(request.user.id))
    else:
        return redirect("./login")

def auth_user(request):
    if request.method == 'POST':
        user_info = json.loads(request.body.decode, encoding='UTF-8')
        user = authenticate(email=user_info["email"], password=user_info["password"])
        if user is not None:
            logout(request)
            login(request, user)
            print(user.email + " logged in")
            return redirect("../"+str(request.user.id))
        else:
            return HttpResponse('not ok')
    else:
        return HttpResponse('not POST')


@csrf_protect
def create_user(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        user_info = json.loads(request.body.decode, encoding='UTF-8')
        user_phone = int(user_info["phone"])
        if user_phone is not None:
            user = User.objects.create_user(email=user_info["email"], password=user_info["password"], phone=user_phone)
            return redirect("../" + str(request.user.id))
        else:
            return HttpResponse("not ok")
    else:
        return HttpResponse('not POST')

def account_info(request, id=0):
    this_user = User.objects.get(id=id)
    return HttpResponse("account page dummy")
