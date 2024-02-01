from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from application.use_cases.tasks import TaskUseCase
from domain.entities.tasks import (
    TaskCreateDTO,
    TaskIdDTO,
    TaskRetrieveDTO,
    TaskUpdateDTO,
)
from infrastructure.permissions.users import IsAdmin

router = APIRouter()


@router.get("/", response_model=list[TaskRetrieveDTO], status_code=HTTP_200_OK)
async def get_all_tasks():
    return await TaskUseCase().get_all()


@router.post("/", response_model=TaskIdDTO, status_code=HTTP_201_CREATED)
async def create_task(new_task: TaskCreateDTO, permission=Depends(IsAdmin())):
    task_id = await TaskUseCase().insert(new_task.model_dump())

    return {"id": task_id}


@router.get("/{task_id}", response_model=TaskRetrieveDTO, status_code=HTTP_200_OK)
async def get_task_by_id(task_id: int):
    return await TaskUseCase().get_by_id(task_id)


@router.put("/{task_id}", status_code=HTTP_204_NO_CONTENT)
async def update_task_by_id(task_id: int, updated_task: TaskUpdateDTO):
    await TaskUseCase().update_by_id(updated_task.model_dump(), task_id)


@router.delete("/{task_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_task_by_id(task_id: int, permission=Depends(IsAdmin())):
    await TaskUseCase().delete_by_id(task_id)
