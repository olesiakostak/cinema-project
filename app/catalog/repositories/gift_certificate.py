from .base import BaseRepository
from app.catalog.models import GiftCertificate

class GiftCertificateRepository(BaseRepository):
    def __init__(self):
        super().__init__(GiftCertificate)