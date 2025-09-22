from .base import BaseRepository
from app.catalog.models import Customer

class CustomerRepository(BaseRepository):
    def __init__(self):
        super().__init__(Customer)
