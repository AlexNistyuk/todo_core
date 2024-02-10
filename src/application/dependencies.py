from dependency_injector import containers, providers

from application.use_cases.interfaces import IUseCase
from application.use_cases.sheets import SheetUseCase
from application.use_cases.tasks import TaskUseCase


class Container(containers.DeclarativeContainer):
    sheet_use_case: IUseCase = providers.Factory(SheetUseCase)
    task_use_case: IUseCase = providers.Factory(TaskUseCase)
