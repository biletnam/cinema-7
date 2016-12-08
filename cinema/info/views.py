from django.http import HttpResponse

def info(request):
    ret_string = 'Test response'
    return HttpResponse(ret_string)
