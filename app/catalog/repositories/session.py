from .base import BaseRepository
from app.catalog.models import Session
from django.db.models.functions import ExtractHour
from django.db.models import Count

class SessionRepository(BaseRepository):
    def __init__(self):
        super().__init__(Session)

    def get_session_time_stats(self):
        return self.get_all().annotate(
            hour=ExtractHour('start_time')
        ).values('hour').annotate(
            num_of_sessions=Count('hour')
        ).order_by('hour')