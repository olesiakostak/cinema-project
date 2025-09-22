from .base import BaseRepository
from app.catalog.models import Payment

class PaymentRepository(BaseRepository):
    def __init__(self):
        super().__init__(Payment)