from infrastructure.models.lists import List
from infrastructure.repositories.base import BaseRepository


class ListRepository(BaseRepository):
    model = List
