from sqlalchemy import Sequence
from sqlalchemy.exc import IntegrityError, NoResultFound

from application.use_cases.interfaces import IUseCase
from domain.exceptions.lists import (
    ListCreateError,
    ListDeleteError,
    ListIntegrityError,
    ListNotFoundError,
    ListRetrieveError,
    ListUpdateError,
)
from infrastructure.models.tasks import Task
from infrastructure.uow.base import UnitOfWork


class ListUseCase(IUseCase):
    """Task use case"""

    uow = UnitOfWork()

    async def insert(self, data: dict) -> int:
        try:
            async with self.uow():
                result = await self.uow.lists.insert(data)
        except IntegrityError:
            raise ListIntegrityError
        except Exception:
            raise ListCreateError
        return result

    async def update_by_id(self, data: dict, list_id: int) -> int:
        try:
            async with self.uow():
                result = await self.uow.lists.update_by_id(data, list_id)
        except NoResultFound:
            raise ListNotFoundError
        except IntegrityError:
            raise ListIntegrityError
        except Exception:
            raise ListUpdateError
        return result

    async def get_all(self) -> Sequence:
        try:
            async with self.uow():
                result = await self.uow.lists.get_all()
        except NoResultFound:
            raise ListNotFoundError
        except Exception:
            raise ListRetrieveError
        return result

    async def get_by_id(self, list_id: int) -> Task:
        try:
            async with self.uow():
                result = await self.uow.lists.get_by_id(list_id)
        except NoResultFound:
            raise ListNotFoundError
        except Exception:
            raise ListRetrieveError
        return result

    async def delete_by_id(self, list_id: int) -> None:
        try:
            async with self.uow():
                await self.uow.lists.delete_by_id(list_id)
        except NoResultFound:
            raise ListNotFoundError
        except Exception:
            raise ListDeleteError
