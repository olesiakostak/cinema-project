from .base import BaseRepository
from app.catalog.models import Ticket

class TicketRepository(BaseRepository):
    def __init__(self):
        super().__init__(Ticket)