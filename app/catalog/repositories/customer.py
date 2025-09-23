from .base import BaseRepository
from app.catalog.models import Customer
from django.db.models import Sum, Count

class CustomerRepository(BaseRepository):
    def __init__(self):
        super().__init__(Customer)

    def get_top_customers(self):
        res = self.get_all().filter(
            payment__operation_type='sale',
            payment__status='success'
            ).annotate(
                purchases_num=Count('payment'),
                total_spend=Sum('payment__ticket__base_price')
                ).values(
                    'id',
                    'first_name',
                    'last_name',
                    'purchases_num',
                    'total_spend'
                ).order_by('-total_spend')
        return res
