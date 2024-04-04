from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from infrastructure.models.tasks import Task, TaskRelationship
from infrastructure.repositories.base import BaseRepository


class TaskRepository(BaseRepository):
    model = Task
    rel_model = TaskRelationship

    async def get_by_sheet_id(self, sheet_id: int, with_joins: bool) -> Sequence:
        if with_joins:
            query = (
                select(self.rel_model)
                .where(self.rel_model.sheet_id == sheet_id)
                .options(
                    joinedload(self.rel_model.sheet), joinedload(self.rel_model.status)
                )
            )
        else:
            query = select(self.model).where(self.model.sheet_id == sheet_id)

        result = await self.session.execute(query)

        return result.scalars().all()

    async def get_all(self, with_joins: bool) -> Sequence:
        if with_joins:
            query = select(self.rel_model).options(
                joinedload(self.rel_model.sheet), joinedload(self.rel_model.status)
            )
        else:
            query = select(self.model)

        result = await self.session.execute(query)

        return result.scalars().all()
