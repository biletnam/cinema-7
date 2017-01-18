from django.http import HttpResponse
from django.shortcuts import render



def show(request,id=0):
    context = {}
    return render(request,'booking/booking.html', context)
