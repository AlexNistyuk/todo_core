from dependency_injector import containers, providers

from application.use_cases.sheets import SheetUseCase
from application.use_cases.tasks import TaskUseCase


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "presentation.api.v1.sheets",
            "presentation.api.v1.tasks",
        ]
    )
    sheet_use_case = providers.Factory(SheetUseCase)
    task_use_case = providers.Factory(TaskUseCase)
