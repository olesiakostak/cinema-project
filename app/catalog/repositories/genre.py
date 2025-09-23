from .base import BaseRepository
from app.catalog.models import Genre
from django.db.models import Count

class GenreRepository(BaseRepository):
    def __init__(self):
        super().__init__(Genre)

    def get_genres_popularity(self):
        return self.get_all().annotate(
            films_count=Count('film')
            ).values(
                'name',
                'films_count'
            ).order_by('-films_count')