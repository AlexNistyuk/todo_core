from dependency_injector import containers, providers

from application.use_cases.interfaces import IUseCase
from application.use_cases.kafka import KafkaUseCase
from application.use_cases.sheets import SheetUseCase
from application.use_cases.tasks import TaskUseCase
from infrastructure.uow.base import UnitOfWork
from infrastructure.uow.interfaces import IUnitOfWork


class Container(containers.DeclarativeContainer):
    kafka_use_case: KafkaUseCase = providers.Factory(KafkaUseCase)
    uow: IUnitOfWork = providers.Factory(UnitOfWork)
    sheet_use_case: IUseCase = providers.Factory(SheetUseCase, uow, kafka_use_case)
    task_use_case: IUseCase = providers.Factory(TaskUseCase, uow, kafka_use_case)
