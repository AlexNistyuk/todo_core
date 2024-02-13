from sqlalchemy import Sequence
from sqlalchemy.exc import IntegrityError, NoResultFound

from application.use_cases.interfaces import IUseCase
from application.use_cases.kafka import KafkaUseCase
from domain.exceptions.sheets import (
    SheetCreateError,
    SheetDeleteError,
    SheetIntegrityError,
    SheetNotFoundError,
    SheetRetrieveError,
    SheetUpdateError,
)
from infrastructure.models.sheets import Sheet
from infrastructure.uow.interfaces import IUnitOfWork


class SheetUseCase(IUseCase):
    """Sheet use case"""

    def __init__(self, uow: IUnitOfWork, kafka_use_case: KafkaUseCase) -> None:
        self.uow = uow
        self.kafka_use_case = kafka_use_case

    async def insert(self, data: dict, user: dict) -> dict:
        try:
            async with self.uow():
                result = await self.uow.sheets.insert(data)
        except IntegrityError:
            raise SheetIntegrityError
        except Exception:
            raise SheetCreateError

        await self.kafka_use_case.send_create_sheet(data.get("name"), user.get("id"))

        return {"id": result}

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

    async def get_by_id(self, sheet_id: int, user: dict) -> Sheet:
        try:
            async with self.uow():
                result = await self.uow.sheets.get_by_id(sheet_id)
        except NoResultFound:
            raise SheetNotFoundError
        except Exception:
            raise SheetRetrieveError

        await self.kafka_use_case.send_retrieve_sheet(result.name, user.get("id"))

        return result

    async def delete_by_id(self, sheet_id: int) -> None:
        try:
            async with self.uow():
                await self.uow.sheets.delete_by_id(sheet_id)
        except NoResultFound:
            raise SheetNotFoundError
        except Exception:
            raise SheetDeleteError
