from django.http import HttpResponse
from django.shortcuts import render

from cinema.schedule.models import Seance, Row


def createRowsList(rowList):
    for row in rowList:
        print(row)
        # for seat in row.seat_count
        # print(row)
    return

def show(request,id=0):
    seance =  Seance.objects.get(id=id)
    hall = seance.hall
    row_count = hall.row_count

    rowList = Row.objects.filter(hall=hall)
    print("RESULT " + str(rowList))

    createRowsList(rowList)

    context = {}
    return render(request,'booking/booking.html', context)


# Руслан Валеев, [12.01.17 14:10]
# {ряд: {место: true, место: false, ...}, ряд: {}, ...}