from django.http import HttpResponse
from django.shortcuts import render

from cinema.schedule.models import Seance


def show(request,id=0):
    seance =  Seance.objects.get(id=id)
    hall = seance.hall
    row_count = hall.row_count
    print("RESULT " + str(row_count))

    context = {}
    return render(request,'booking/booking.html', context)
