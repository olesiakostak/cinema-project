from .base import BaseRepository
from app.catalog.models import Hall
from django.db.models import Count

class HallRepository(BaseRepository):
    def __init__(self):
        super().__init__(Hall)

    def get_hall_stats(self):
        return self.get_all().annotate(
            sessions_count=Count('session')
        ).values(
            'name',
            'screen_type',
            'sessions_count'
        ).order_by('-sessions_count')