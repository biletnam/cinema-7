from django.http import HttpResponse

# Create your views here.

def index(request, num = "1"):
    return HttpResponse('hello')