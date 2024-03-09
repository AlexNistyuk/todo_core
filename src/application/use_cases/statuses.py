from sqlalchemy import Sequence
from sqlalchemy.exc import IntegrityError, NoResultFound

from application.use_cases.interfaces import IUseCase
from domain.exceptions.statuses import (
    StatusCreateError,
    StatusDeleteError,
    StatusIntegrityError,
    StatusNotFoundError,
    StatusRetrieveError,
    StatusUpdateError,
)
from infrastructure.models.statuses import Status
from infrastructure.uow.interfaces import IUnitOfWork


class StatusUseCase(IUseCase):
    """Status use case"""

    def __init__(self, uow: IUnitOfWork) -> None:
        self.uow = uow

    async def insert(self, data: dict) -> None:
        try:
            async with self.uow():
                await self.uow.statuses.insert_many(**data)
        except IntegrityError:
            raise StatusIntegrityError
        except Exception:
            raise StatusCreateError

    async def update_by_id(self, data: dict, status_id: int) -> Status:
        try:
            async with self.uow():
                result = await self.uow.statuses.update_by_id(data, status_id)
        except NoResultFound:
            raise StatusNotFoundError
        except IntegrityError:
            raise StatusIntegrityError
        except Exception:
            raise StatusUpdateError
        return result

    async def get_all(self) -> Sequence:
        try:
            async with self.uow():
                result = await self.uow.statuses.get_all()
        except NoResultFound:
            raise StatusNotFoundError
        except Exception:
            raise StatusRetrieveError
        return result

    async def get_by_id(self, status_id: int) -> Status:
        try:
            async with self.uow():
                result = await self.uow.statuses.get_by_id(status_id)
        except NoResultFound:
            raise StatusNotFoundError
        except Exception:
            raise StatusRetrieveError
        return result

    async def get_first_status_id(self, sheet_id: int) -> int:
        try:
            async with self.uow():
                status_id = await self.uow.statuses.get_first_status_id(sheet_id)
        except NoResultFound:
            raise StatusNotFoundError
        except Exception:
            raise StatusRetrieveError
        return status_id

    async def delete_by_id(self, status_id: int) -> None:
        try:
            async with self.uow():
                await self.uow.statuses.delete_by_id(status_id)
        except NoResultFound:
            raise StatusNotFoundError
        except Exception:
            raise StatusDeleteError
