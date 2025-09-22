from .base import BaseRepository
from app.catalog.models import Session

class SessionRepository(BaseRepository):
    def __init__(self):
        super().__init__(Session)