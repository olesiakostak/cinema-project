from .base import BaseRepository
from app.catalog.models import Film
from django.db.models import Count, Sum

class FilmRepository(BaseRepository):
    def __init__(self):
        super().__init__(Film)

    def get_performance_stats(self):
        res = self.get_all().annotate(
            total_sessions=Count('session', distinct=True),
            number_of_sold_tickets=Count('session__ticket'),
            total_revenue=Sum('session__ticket__base_price')
            ).values(
                'title',
                'rating',
                'total_sessions',
                'number_of_sold_tickets',
                'total_revenue'
            )
        return res