from django.shortcuts import render, HttpResponse, redirect
from cinema.account.models import User
from cinema.booking.models import Booking
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

def redirect_to_self(request):
    if request.user.is_authenticated():
        return redirect("./"+str(request.user.id))
    else:
        return redirect("login-url")

def auth_user(request):
    if request.method == 'POST':
        user_info = request.POST
        user = authenticate(email=user_info["email"], password=user_info["password"])
        if user is not None:
            logout(request)
            login(request, user)
            return redirect("to-self")
        else:
            return redirect("su_error")
    else:
        return HttpResponse("not POST")

def logout_user(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            logout(request)
    return(redirect("../../../"))

def create_user(request):
    if request.method == 'POST':
        user_info = request.POST
        user_phone = user_info["phone"]
        if user_phone is not None:
            User.objects.create_user(email=user_info["email"], password=user_info["password"], phone=user_phone)
            user = authenticate(email=user_info["email"], password=user_info["password"])
            login(request, user)
            return redirect("to-self")
        else:
            return redirect()
    else:
        return HttpResponse('not POST')

def account_info(request, id=0):
    if request.user.is_authenticated():
        if int(request.user.id) == int(id):
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
                booking["time"] = entity.seance.start_time
                booking["movie"] = entity.seance.movie.id
                bookings.append(booking)
            response["booking"] = bookings
            return render(request, "account_info.html", context=response)
        else:
            return redirect("to-self")
    else:
        return redirect("login-url")

def signup_error(request):
    return(render(request, "signup_error.html"))

def signin_error(request):
    return(render(request, "signin_error.html"))