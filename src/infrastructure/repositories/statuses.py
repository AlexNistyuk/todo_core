from sqlalchemy import select

from infrastructure.models.statuses import Status
from infrastructure.repositories.base import BaseRepository


class StatusRepository(BaseRepository):
    model = Status

    async def insert_many(self, sheet_id: int, names: list[str]) -> None:
        statuses = [self.model(name=name, sheet_id=sheet_id) for name in names]

        self.session.add_all(statuses)

    async def get_first_status_id(self, sheet_id: int) -> int:
        query = (
            select(self.model.id)
            .filter_by(sheet_id=sheet_id)
            .limit(1)
            .order_by(self.model.id)
        )
        result = await self.session.execute(query)

        return result.scalar_one()
