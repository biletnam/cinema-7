import json

from django.http import HttpResponse
from django.middleware.common import logger
from django.shortcuts import render
from cinema.booking.models import Booking
from cinema.schedule.models import Seance, Row, Seat


def show(request, id=0):
    result = {}

    seance = Seance.objects.get(id=id)
    hall = seance.hall

    rowList = Row.objects.filter(hall=hall)

    for row in rowList:
        seatList = []
        for i in range(1, row.seat_count + 1):
            seat = Seat(Seat.objects.filter(hall=hall, row=row, number=i, seance=seance))
            seatList.append(seat.booked)
        result.update({row.number: seatList})

    context = {'result': result, 'seance': seance}
    return render(request, 'booking/index.html', context)


def show_booking_info(request, id=0):
    booking = Booking.objects.get(id=id)
    seance = booking.seance
    context = {
        'booking': booking,
        'seance': seance,
    }
    return render(request, 'booking/booking_info.html',context)

def create_booking(request):
    if request.is_ajax():
        if request.method == 'POST':
            jsonResponse = json.loads(request.body.decode(encoding='UTF-8'))

            seance = Seance.objects.get(id=jsonResponse.get("seance"))
            bookingList = jsonResponse.get("selected")
            price = jsonResponse.get("price")

            booking = Booking.objects.create(price=price, seance=seance, seats=bookingList)
            response_data = {}
            response_data["booking_id"] = booking.get_id()

            return (HttpResponse(json.dumps(response_data), content_type = "application/json", status=200))
    else:
        return (HttpResponse(status=404))