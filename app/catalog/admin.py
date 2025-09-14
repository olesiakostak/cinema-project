from django.contrib import admin
from django.db import models
from .models import Film, Genre, Hall, Customer, GiftCertificate, Seat, Session, Ticket, Payment

admin.site.register(Genre)
admin.site.register(Film)
admin.site.register(Customer)
admin.site.register(Hall)
admin.site.register(GiftCertificate)
admin.site.register(Seat)
admin.site.register(Session)
admin.site.register(Ticket)
admin.site.register(Payment)