from sqlalchemy import Sequence
from sqlalchemy.exc import IntegrityError, NoResultFound

from application.use_cases.interfaces import IUseCase
from domain.exceptions.sheets import (
    SheetCreateError,
    SheetDeleteError,
    SheetIntegrityError,
    SheetNotFoundError,
    SheetRetrieveError,
    SheetUpdateError,
)
from infrastructure.models.tasks import Task
from infrastructure.uow.base import UnitOfWork


class SheetUseCase(IUseCase):
    """Sheet use case"""

    uow = UnitOfWork()

    async def insert(self, data: dict) -> int:
        try:
            async with self.uow():
                result = await self.uow.sheets.insert(data)
        except IntegrityError:
            raise SheetIntegrityError
        except Exception:
            raise SheetCreateError
        return result

    async def update_by_id(self, data: dict, sheet_id: int) -> int:
        try:
            async with self.uow():
                result = await self.uow.sheets.update_by_id(data, sheet_id)
        except NoResultFound:
            raise SheetNotFoundError
        except IntegrityError:
            raise SheetIntegrityError
        except Exception:
            raise SheetUpdateError
        return result

    async def get_all(self) -> Sequence:
        try:
            async with self.uow():
                result = await self.uow.sheets.get_all()
        except NoResultFound:
            raise SheetNotFoundError
        except Exception:
            raise SheetRetrieveError
        return result

    async def get_by_id(self, sheet_id: int) -> Task:
        try:
            async with self.uow():
                result = await self.uow.sheets.get_by_id(sheet_id)
        except NoResultFound:
            raise SheetNotFoundError
        except Exception:
            raise SheetRetrieveError
        return result

    async def delete_by_id(self, sheet_id: int) -> None:
        try:
            async with self.uow():
                await self.uow.sheets.delete_by_id(sheet_id)
        except NoResultFound:
            raise SheetNotFoundError
        except Exception:
            raise SheetDeleteError
