from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<p>test</p>")

def show(request,id=0):
    context = {}
    return render('booking/index.html', context)
