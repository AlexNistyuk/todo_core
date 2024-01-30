from sqlalchemy import Sequence
from sqlalchemy.exc import IntegrityError, NoResultFound

from application.use_cases.interfaces import IUseCase
from domain.exceptions.tasks import (
    TaskCreateError,
    TaskDeleteError,
    TaskIntegrityError,
    TaskNotFoundError,
    TaskRetrieveError,
    TaskUpdateError,
)
from infrastructure.models.tasks import Task
from infrastructure.uow.base import UnitOfWork


class TaskUseCase(IUseCase):
    """Task use case"""

    uow = UnitOfWork()

    async def insert(self, data: dict) -> int:
        try:
            async with self.uow():
                result = await self.uow.tasks.insert(data)
        except IntegrityError:
            raise TaskIntegrityError
        except Exception:
            raise TaskCreateError
        return result

    async def update_by_id(self, data: dict, task_id: int) -> int:
        try:
            async with self.uow():
                result = await self.uow.tasks.update_by_id(data, task_id)
        except NoResultFound:
            raise TaskNotFoundError
        except IntegrityError:
            raise TaskIntegrityError
        except Exception:
            raise TaskUpdateError
        return result

    async def get_all(self) -> Sequence:
        try:
            async with self.uow():
                result = await self.uow.tasks.get_all()
        except NoResultFound:
            raise TaskNotFoundError
        except Exception:
            raise TaskRetrieveError
        return result

    async def get_by_id(self, task_id: int) -> Task:
        try:
            async with self.uow():
                result = await self.uow.tasks.get_by_id(task_id)
        except NoResultFound:
            raise TaskNotFoundError
        except Exception:
            raise TaskRetrieveError
        return result

    async def delete_by_id(self, task_id: int) -> None:
        try:
            async with self.uow():
                await self.uow.tasks.delete_by_id(task_id)
        except NoResultFound:
            raise TaskNotFoundError
        except Exception:
            raise TaskDeleteError
