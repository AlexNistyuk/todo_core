import enum

from infrastructure.repositories.kafka import KafkaRepository


class ActionType(enum.Enum):
    create = "create"
    retrieve = "retrieve"
    done = "done"


class KafkaUseCase:
    repository = KafkaRepository()

    async def send_create_task(self, name: str, user_id: int) -> None:
        await self.__send_task_message(name, ActionType.create.value, user_id)

    async def send_retrieve_task(self, name: str, user_id: int) -> None:
        await self.__send_task_message(name, ActionType.retrieve.value, user_id)

    async def send_done_task(self, name: str, user_id: int) -> None:
        await self.__send_task_message(name, ActionType.done.value, user_id)

    async def send_create_sheet(self, name: str, user_id: int) -> None:
        await self.__send_sheet_message(name, ActionType.create.value, user_id)

    async def send_retrieve_sheet(self, name: str, user_id: int) -> None:
        await self.__send_sheet_message(name, ActionType.retrieve.value, user_id)

    async def __send_task_message(self, name: str, action_at: str, user_id: int):
        await self.__send_message(name, action_at, user_id, "task")

    async def __send_sheet_message(self, name: str, action_at: str, user_id: int):
        await self.__send_message(name, action_at, user_id, "sheet")

    async def __send_message(
        self, name: str, action_at: str, user_id: int, action_type: str
    ):
        message = {
            "action_at": action_at,
            "name": name,
            "user_id": user_id,
            "action_type": action_type,
        }

        await self.repository.send_message(message)
