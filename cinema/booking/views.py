import json

from django.db import connection
from django.http import HttpResponse
from django.middleware.common import logger
from django.shortcuts import render
from cinema.booking.models import Booking
from cinema.account.models import User
from cinema.schedule.models import Seance, Row, Seat


def show(request, id=0):
    dictJSON = {}

    seance = Seance.objects.get(id=id)
    hall = seance.hall

    rowList = Row.objects.filter(hall=hall)

    for row in rowList:
        seatList = []
        for i in range(1, row.seat_count + 1):
            seat = Seat.objects.get(hall=hall, row=row, number=i, seance=seance)
            seatList.append(seat.booked)
        dictJSON.update({str(row.number): seatList})

    resultJSON = json.dumps(dictJSON)

    context = {'result': resultJSON, 'seance': seance}
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
            #collecting data to create booking
            json_request = json.loads(request.body.decode(encoding='UTF-8'))
            seance = Seance.objects.get(id=json_request.get("seance"))
            bookingList = json_request.get("selected")
            price = json_request.get("price")
            user = User.objects.get(id=request.user.id)
            #creating new Booking instance
            booking = Booking.objects.create(price=price, seance=seance, seats=bookingList, user=user)

            #collecting response data - booking_id
            response_data = {}
            response_data["booking_id"] = booking.get_id()

            # next update data in Seats table
            hall = seance.hall
            #do this for each selected seat
            for seat in bookingList:
                indices = seat.split("_")
                row = Row.objects.filter(hall=hall, number = int(indices[0]))
                number = int(indices[1])
                Seat.objects.filter(seance=seance, hall=hall, row=row, number=number).update(booked=True)

            connection.close()
            return (HttpResponse(json.dumps(response_data), content_type = "application/json", status=200))
    else:
        return (HttpResponse(status=404))