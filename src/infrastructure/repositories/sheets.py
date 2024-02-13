from infrastructure.models.sheets import Sheet
from infrastructure.repositories.base import BaseRepository


class SheetRepository(BaseRepository):
    model = Sheet
