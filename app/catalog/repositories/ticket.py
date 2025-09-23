from .base import BaseRepository
from app.catalog.models import Ticket

class TicketRepository(BaseRepository):
    def __init__(self):
        super().__init__(Ticket)
    
    def get_booked_tickets(self):
        return self.get_all().filter(
            status='booked'
        )