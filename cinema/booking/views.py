from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from cinema.booking.models import Booking
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


    context = {'result': result, 'seance': seance}
    return render(request,'booking/index.html', context)

# class booking_info(generic.DetailView):
#         model = Booking
#         template_name = 'booking/booking_info.html'

def show_booking_info(request,id=0):
    booking = Booking.objects.get(id=id)
    context = {'booking': booking}
    return render(request, 'booking/booking_info.html', context)


# Руслан Валеев, [12.01.17 14:10]
# {ряд: {место: true, место: false, ...}, ряд: {}, ...}