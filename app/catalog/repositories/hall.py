from .base import BaseRepository
from app.catalog.models import Hall

class HallRepository(BaseRepository):
    def __init__(self):
        super().__init__(Hall)