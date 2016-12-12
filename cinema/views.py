from django.shortcuts import render

def call404(request):
    return render(request, template_name="404.html")