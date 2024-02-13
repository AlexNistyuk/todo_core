from domain.enums.sheets import SheetActionType
from domain.enums.tasks import TaskActionType
from infrastructure.managers.kafka import KafkaManager


class KafkaUseCase(KafkaManager):
    async def send_create_task(self, name: str, user_id: int) -> None:
        await self.__send_task_message(name, TaskActionType.create.value, user_id)

    async def send_retrieve_task(self, name: str, user_id: int) -> None:
        await self.__send_task_message(name, TaskActionType.retrieve.value, user_id)

    async def send_done_task(self, name: str, user_id: int) -> None:
        await self.__send_task_message(name, TaskActionType.done.value, user_id)

    async def send_create_sheet(self, name: str, user_id: int) -> None:
        await self.__send_sheet_message(name, SheetActionType.create.value, user_id)

    async def send_retrieve_sheet(self, name: str, user_id: int) -> None:
        await self.__send_sheet_message(name, SheetActionType.retrieve.value, user_id)

    async def __send_task_message(self, name: str, action_at: str, user_id: int):
        await self.__send_message(name, "task", user_id, action_at)

    async def __send_sheet_message(self, name: str, action_at: str, user_id: int):
        await self.__send_message(name, "sheet", user_id, action_at)

    async def __send_message(
        self, name: str, action_at: str, user_id: int, action_type: str
    ):
        message = {
            "action_at": action_at,
            "name": name,
            "user_id": user_id,
            "action_type": action_type,
        }

        await self.send_message(message)
