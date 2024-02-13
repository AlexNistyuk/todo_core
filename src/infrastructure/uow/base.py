from infrastructure.managers.database import DatabaseManager
from infrastructure.repositories.sheets import SheetRepository
from infrastructure.repositories.tasks import TaskRepository
from infrastructure.uow.interfaces import IUnitOfWork


class UnitOfWork(DatabaseManager, IUnitOfWork):
    """Unit of work"""

    def __init__(self):
        self.session_factory = self.async_session_maker

    def __call__(self, autocommit: bool = True):
        self._autocommit = autocommit

        return self

    async def __aenter__(self):
        self.session = self.session_factory()
        self.sheets = SheetRepository(self.session)
        self.tasks = TaskRepository(self.session)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            if self._autocommit:
                await self.commit()
        else:
            await self.rollback()

        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
