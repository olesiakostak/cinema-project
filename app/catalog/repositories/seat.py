from .base import BaseRepository
from app.catalog.models import Seat

class SeatRepository(BaseRepository):
    def __init__(self):
        super().__init__(Seat)