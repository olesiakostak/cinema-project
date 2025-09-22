from .base import BaseRepository
from app.catalog.models import Film

class FilmRepository(BaseRepository):
    def __init__(self):
        super().__init__(Film)