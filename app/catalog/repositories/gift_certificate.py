from .base import BaseRepository
from app.catalog.models import GiftCertificate
from django.db.models import Count

class GiftCertificateRepository(BaseRepository):
    def __init__(self):
        super().__init__(GiftCertificate)

    def get_usage_stats(self):
        return self.get_all().annotate(
            usage_count=Count('payment')
            ).values(
                'code', 
                'usage_count'
            ).order_by('-usage_count')

    