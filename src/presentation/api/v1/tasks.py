from fastapi import APIRouter, Depends
from starlette.requests import Request
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from application.use_cases.kafka import KafkaUseCase
from application.use_cases.tasks import TaskUseCase
from domain.entities.tasks import (
    TaskCreateDTO,
    TaskIdDTO,
    TaskRetrieveDTO,
    TaskUpdateDTO,
)
from infrastructure.models.tasks import TaskStatus
from infrastructure.permissions.users import IsAdmin

router = APIRouter()


@router.get("/", response_model=list[TaskRetrieveDTO], status_code=HTTP_200_OK)
async def get_all_tasks():
    return await TaskUseCase().get_all()


@router.post("/", response_model=TaskIdDTO, status_code=HTTP_201_CREATED)
async def create_task(
    request: Request, new_task: TaskCreateDTO, permission=Depends(IsAdmin())
):
    task_id = await TaskUseCase().insert(new_task.model_dump())
    await KafkaUseCase().send_create_task(new_task.name, request.state.user.get("id"))

    return {"id": task_id}


@router.get("/{task_id}", response_model=TaskRetrieveDTO, status_code=HTTP_200_OK)
async def get_task_by_id(request: Request, task_id: int):
    task = await TaskUseCase().get_by_id(task_id)
    await KafkaUseCase().send_retrieve_task(task.name, request.state.user.get("id"))

    return task


@router.put("/{task_id}", status_code=HTTP_204_NO_CONTENT)
async def update_task_by_id(task_id: int, updated_task: TaskUpdateDTO):
    await TaskUseCase().update_by_id(updated_task.model_dump(), task_id)


@router.patch("/{task_id}", status_code=HTTP_204_NO_CONTENT)
async def done_task_by_id(request: Request, task_id: int):
    data = {"status": TaskStatus.done.value}

    task = await TaskUseCase().update_by_id(data, task_id)
    await KafkaUseCase().send_done_task(task.name, request.state.user.get("id"))


@router.delete("/{task_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_task_by_id(task_id: int, permission=Depends(IsAdmin())):
    await TaskUseCase().delete_by_id(task_id)
