from django.contrib import admin
from .models import Booking, Booking_new

admin.site.register(Booking, Booking_new)
