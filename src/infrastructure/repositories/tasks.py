from typing import Sequence

from sqlalchemy import select

from infrastructure.models.tasks import Task
from infrastructure.repositories.base import BaseRepository


class TaskRepository(BaseRepository):
    model = Task

    async def get_by_sheet_id(self, sheet_id: int) -> Sequence[Task]:
        query = select(self.model).where(self.model.sheet_id == sheet_id)
        result = await self.session.execute(query)

        return result.scalars().all()
