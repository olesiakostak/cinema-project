from django.db import models
from .models import Film, Genre, Hall, Customer, GiftCertificate, Seat, Session, Ticket, Payment

class BaseRepository:
    def __init__(self, model: models.Model):
        self.model = model

    def get_all(self):
        return self.model.objects.all()
    
    def get_by_id(self, obj_id):
        try:
            return self.model.objects.get(id=obj_id)
        except self.model.DoesNotExist:
            return None
    
    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)
    
class GenreRepository(BaseRepository):
    def __init__(self):
        super().__init__(Genre)

class FilmRepository(BaseRepository):
    def __init__(self):
        super().__init__(Film)

class HallRepository(BaseRepository):
    def __init__(self):
        super().__init__(Hall)

class CustomerRepository(BaseRepository):
    def __init__(self):
        super().__init__(Customer)

class GiftCertificateRepository(BaseRepository):
    def __init__(self):
        super().__init__(GiftCertificate)

class SeatRepository(BaseRepository):
    def __init__(self):
        super().__init__(Seat)

class SessionRepository(BaseRepository):
    def __init__(self):
        super().__init__(Session)

class TicketRepository(BaseRepository):
    def __init__(self):
        super().__init__(Ticket)

class PaymentRepository(BaseRepository):
    def __init__(self):
        super().__init__(Payment)

class UnitOfWork:
    def __init__(self):
        self.genres = GenreRepository()
        self.films = FilmRepository()
        self.halls = HallRepository()
        self.customers = CustomerRepository()
        self.gift_certificates = GiftCertificateRepository()
        self.seats = SeatRepository()
        self.sessions = SessionRepository()
        self.tickets = TicketRepository()
        self.payments = PaymentRepository()

unit_of_work = UnitOfWork()
