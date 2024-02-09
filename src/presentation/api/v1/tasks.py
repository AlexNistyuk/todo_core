from fastapi import APIRouter, Depends
from starlette.requests import Request
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_503_SERVICE_UNAVAILABLE,
)

from application.use_cases.tasks import TaskUseCase
from domain.entities.tasks import (
    TaskCreateDTO,
    TaskIdDTO,
    TaskRetrieveDTO,
    TaskUpdateDTO,
)
from infrastructure.permissions.users import IsAdmin

router = APIRouter()


@router.get(
    "/",
    response_model=list[TaskRetrieveDTO],
    status_code=HTTP_200_OK,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def get_all_tasks():
    return await TaskUseCase().get_all()


@router.post(
    "/",
    response_model=TaskIdDTO,
    status_code=HTTP_201_CREATED,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def create_task(
    request: Request, new_task: TaskCreateDTO, permission=Depends(IsAdmin())
):
    return await TaskUseCase().insert(new_task.model_dump(), request.state.user)


@router.get(
    "/{task_id}",
    response_model=TaskRetrieveDTO,
    status_code=HTTP_200_OK,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def get_task_by_id(request: Request, task_id: int):
    return await TaskUseCase().get_by_id(task_id, request.state.user)


@router.put(
    "/{task_id}",
    status_code=HTTP_204_NO_CONTENT,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def update_task_by_id(
    task_id: int, updated_task: TaskUpdateDTO, permission=Depends(IsAdmin())
):
    await TaskUseCase().update_by_id(updated_task.model_dump(), task_id)


@router.patch(
    "/{task_id}",
    status_code=HTTP_204_NO_CONTENT,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def done_task_by_id(request: Request, task_id: int):
    return await TaskUseCase().done_by_id(task_id, request.state.user)


@router.delete(
    "/{task_id}",
    status_code=HTTP_204_NO_CONTENT,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def delete_task_by_id(task_id: int, permission=Depends(IsAdmin())):
    await TaskUseCase().delete_by_id(task_id)
