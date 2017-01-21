from django.db import models
from cinema.catalog.models import Movie
import datetime


class Hall(models.Model):
    name = models.CharField(max_length=200)
    row_count = models.IntegerField(default=0)
    seats_in_row = models.IntegerField(default=10)

    def __str__(self):
        return self.name

    def create_rows(self):
        rows_list = []
        for i in range(1, self.row_count + 1):
            row = Row(hall=self, number=i, seat_count=self.seats_in_row)
            rows_list.append(row)
        Row.objects.bulk_create(rows_list)

    def save(self, *args, **kwargs):
        super(Hall, self).save(*args, **kwargs)
        self.create_rows()


class Row(models.Model):
    hall = models.ForeignKey(Hall)
    number = models.IntegerField()
    seat_count = models.IntegerField()

    def __str__(self):
        return "%s %d" % (self.hall.name, self.number)


class Seance(models.Model):
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False, editable=False)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return self.movie.title + " " + self.hall.name

    def create_seats(self):
        seats_list = []
        rows = list(Row.objects.filter(hall=self.hall))

        for row in rows:
            for i in range(1, row.seat_count + 1):
                seat = Seat(hall = self.hall, row = row, number=i, seance = self, booked=False)
                seats_list.append(seat)

        Seat.objects.bulk_create(seats_list)

    def save(self, *args, **kwargs):
        self.end_time = self.start_time + datetime.timedelta(minutes = self.movie.duration)
        super(Seance, self).save(*args, **kwargs)
        self.create_seats()


class Seat(models.Model):
    hall = models.ForeignKey(Hall)
    row = models.ForeignKey(Row)
    number = models.IntegerField(default=0)
    seance = models.ForeignKey(Seance)
    booked = models.BooleanField(default=False)

    def __str__(self):
        return "%s: %d-%d %b" % (self.hall.name, self.row.number, self.number)


