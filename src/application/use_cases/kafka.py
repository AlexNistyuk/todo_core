import enum

from infrastructure.repositories.kafka import KafkaRepository


class Action(enum.Enum):
    create = "create"
    retrieve = "retrieve"
    done = "done"


class KafkaUseCase:
    repository = KafkaRepository()

    async def send_creating_task(self, name: str, user_id: int) -> None:
        await self.__send_task_message(name, Action.create.value, user_id)

    async def send_getting_task(self, name: str, user_id: int) -> None:
        await self.__send_task_message(name, Action.retrieve.value, user_id)

    async def send_done_task(self, name: str, user_id: int) -> None:
        await self.__send_task_message(name, Action.done.value, user_id)

    async def send_creating_sheet(self, name: str, user_id: int) -> None:
        await self.__send_sheet_message(name, Action.create.value, user_id)

    async def send_getting_sheet(self, name: str, user_id: int) -> None:
        await self.__send_sheet_message(name, Action.retrieve.value, user_id)

    async def __send_task_message(self, name: str, action: str, user_id: int):
        await self.__send_message(name, action, user_id, "task")

    async def __send_sheet_message(self, name: str, action: str, user_id: int):
        await self.__send_message(name, action, user_id, "sheet")

    async def __send_message(self, name: str, action: str, user_id: int, obj_type: str):
        message = {"action": action, "name": name, "user_id": user_id, "type": obj_type}

        await self.repository.send_message(message)
