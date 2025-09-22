from .base import BaseRepository
from .customer import CustomerRepository
from .film import FilmRepository
from .genre import GenreRepository
from .gift_certificate import GiftCertificateRepository
from .hall import HallRepository
from .payment import PaymentRepository
from .seat import SeatRepository
from .session import SessionRepository
from .ticket import TicketRepository

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

