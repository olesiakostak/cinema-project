from .base import BaseRepository
from app.catalog.models import Payment

class PaymentRepository(BaseRepository):
    def __init__(self):
        super().__init__(Payment)

    def get_successful_payments(self):
        return self.get_all().filter(
            status='success'
        )

    def get_fail_payments(self):
        return self.get_all().filter(
            status='fail'
        )