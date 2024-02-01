import enum

from infrastructure.repositories.kafka import KafkaRepository


class Action(enum.Enum):
    delete_task = "delete task"
    create_task = "create task"
    done_task = "done task"
    create_sheet = "create sheet"
    delete_sheet = "delete sheet"


class KafkaUseCase:
    repository = KafkaRepository()

    async def send_creating_task(self, user_id: int) -> None:
        await self.__send_message(Action.create_task.value, user_id)

    async def send_deleting_task(self, user_id: int) -> None:
        await self.__send_message(Action.delete_task.value, user_id)

    async def send_done_task(self, user_id: int) -> None:
        await self.__send_message(Action.done_task.value, user_id)

    async def send_creating_sheet(self, user_id: int) -> None:
        await self.__send_message(Action.create_sheet.value, user_id)

    async def send_deleting_sheet(self, user_id: int) -> None:
        await self.__send_message(Action.delete_sheet.value, user_id)

    async def __send_message(self, action: str, user_id: int):
        message = {"action": action, "user_id": user_id}

        await self.repository.send_message(message)
