from django.http import HttpResponse
from django.shortcuts import render

from cinema.schedule.models import Seance, Row, Seat

def show(request,id=0):
    result = {}

    seance =  Seance.objects.get(id=id)
    hall = seance.hall

    rowList = Row.objects.filter(hall=hall)

    for row in rowList:
        seatList = []
        for i in range(1, row.seat_count + 1):
            seat = Seat(Seat.objects.filter(hall=hall, row=row, number=i, seance=seance))
            seatList.append(seat.booked)
        result.update({row.number: seatList})


    context = {'result': result}
    return render(request,'booking/index.html', context)


# Руслан Валеев, [12.01.17 14:10]
# {ряд: {место: true, место: false, ...}, ряд: {}, ...}