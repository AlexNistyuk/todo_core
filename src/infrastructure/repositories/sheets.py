from sqlalchemy import func, select

from infrastructure.models.sheets import Sheet
from infrastructure.models.statuses import Status
from infrastructure.models.tasks import Task
from infrastructure.repositories.base import BaseRepository


class SheetRepository(BaseRepository):
    model = Sheet

    async def get_all(self, with_count: bool = False):
        if with_count:
            subqueries = (
                select(func.count()).where(Task.sheet_id == Sheet.id).as_scalar(),
                select(func.count()).where(Status.sheet_id == Sheet.id).as_scalar(),
            )

            query = select(self.model, *subqueries).order_by(self.model.id)
        else:
            query = select(self.model).order_by(self.model.id)

        result = await self.session.execute(query)

        if with_count:
            return result.all()
        return result.scalars().all()
