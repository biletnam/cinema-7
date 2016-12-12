from django.shortcuts import render, HttpResponse

def call404(request):
     return render(request, template_name="global/404.html")
