from typing import Sequence

from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.repositories.interfaces import IRepository


class BaseRepository(IRepository):
    """Base repository"""

    model = None

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def insert(self, data: dict) -> int:
        query = insert(self.model).values(**data).returning(self.model.id)
        result = await self.session.execute(query)

        return result.scalar_one()

    async def update_by_id(self, data: dict, record_id: int) -> int:
        query = (
            update(self.model)
            .values(**data)
            .filter_by(id=record_id)
            .returning(self.model.id)
        )
        result = await self.session.execute(query)

        return result.scalar_one()

    async def get_all(self) -> Sequence:
        query = select(self.model)
        result = await self.session.execute(query)

        return result.scalars().all()

    async def get_by_id(self, record_id: int) -> dict:
        query = select(self.model).filter_by(id=record_id)
        result = await self.session.execute(query)

        return result.scalar_one()

    async def delete_by_id(self, record_id: int) -> int:
        query = delete(self.model).filter_by(id=record_id).returning(self.model.id)
        result = await self.session.execute(query)

        return result.scalar_one()
