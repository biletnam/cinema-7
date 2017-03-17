from django.shortcuts import render, HttpResponse, redirect
from cinema.account.models import User
from cinema.booking.models import Booking
from django.contrib.auth import authenticate, login, logout
import json


def login_view(request):
    return render(request, 'login.html')


def signup_view(request):
    return render(request, 'signup.html')

def redirect_to_self(request):
    if request.user.is_authenticated():
        return redirect("./"+str(request.user.id))
    else:
        return redirect("./login")

def auth_user(request):
    if request.method == 'POST':
        user_info = request.POST
        user = authenticate(email=user_info["email"], password=user_info["password"])
        if user is not None:
            logout(request)
            login(request, user)
            print(user.email + " logged in")
            return redirect("../../"+str(request.user.id))
        else:
            return HttpResponse('not ok')
    else:
        return HttpResponse('not POST')

def create_user(request):
    if request.method == 'POST':
        user_info = request.POST
        user_phone = int(user_info["phone"])
        if user_phone is not None:
            user = User.objects.create_user(email=user_info["email"], password=user_info["password"], phone=user_phone)
            return redirect("../../" + str(user.id))
        else:
            return HttpResponse("not ok")
    else:
        return HttpResponse('not POST')

def account_info(request, id=0):
    this_user = User.objects.get(id=id)

    response = {}
    response["username"] = this_user.email
    response["phone"] = this_user.phone

    bookings = []
    queryset = Booking.objects.filter(user=this_user.id)
    for entity in queryset:
        booking = {}
        booking["id"] = entity.id
        booking["title"] = entity.seance.movie.title
        booking["time"] = entity.seance.start_time.timestamp()
        bookings.append(booking)
    response["booking"] = bookings

    return render(request, "account_info.html", context=response)
