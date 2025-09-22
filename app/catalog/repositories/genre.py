from .base import BaseRepository
from app.catalog.models import Genre

class GenreRepository(BaseRepository):
    def __init__(self):
        super().__init__(Genre)