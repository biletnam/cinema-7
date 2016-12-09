from django.shortcuts import render
from .models import Cinema

def info(request):
    cinema_info = Cinema.objects.first()
    context = {'cinema_info': cinema_info}
    return render(request, 'info/index.html', context)
