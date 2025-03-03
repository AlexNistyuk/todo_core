from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette.requests import Request
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_503_SERVICE_UNAVAILABLE,
)

from application.dependencies import Container
from domain.entities.tasks import (
    TaskCreateDTO,
    TaskIdDTO,
    TaskRetrieveDTO,
    TaskUpdateDTO,
    TaskUpdateStatusDTO,
)

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
@inject
async def get_all_tasks(
    sheet_id: int | None = None,
    with_joins: bool = False,
    task_use_case=Depends(Provide[Container.task_use_case]),
):
    if sheet_id is None:
        return await task_use_case.get_all(with_joins)
    return await task_use_case.get_by_sheet_id(sheet_id, with_joins)


@router.post(
    "/",
    response_model=TaskIdDTO,
    status_code=HTTP_201_CREATED,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
@inject
async def create_task(
    request: Request,
    new_task: TaskCreateDTO,
    task_use_case=Depends(Provide[Container.task_use_case]),
):
    return await task_use_case.insert(new_task.model_dump(), request.state.user)


@router.get(
    "/{task_id}/",
    response_model=TaskRetrieveDTO,
    status_code=HTTP_200_OK,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
@inject
async def get_task_by_id(
    request: Request,
    task_id: int,
    task_use_case=Depends(Provide[Container.task_use_case]),
):
    return await task_use_case.get_by_id(task_id, request.state.user)


@router.put(
    "/{task_id}/",
    status_code=HTTP_204_NO_CONTENT,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
@inject
async def update_task_by_id(
    task_id: int,
    updated_task: TaskUpdateDTO,
    task_use_case=Depends(Provide[Container.task_use_case]),
):
    await task_use_case.update_by_id(updated_task.model_dump(), task_id)


@router.patch(
    "/{task_id}/",
    status_code=HTTP_204_NO_CONTENT,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
@inject
async def update_task_status_by_id(
    new_status: TaskUpdateStatusDTO,
    task_id: int,
    task_use_case=Depends(Provide[Container.task_use_case]),
):
    await task_use_case.update_status_by_id(new_status.model_dump(), task_id)


@router.delete(
    "/{task_id}/",
    status_code=HTTP_204_NO_CONTENT,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
@inject
async def delete_task_by_id(
    task_id: int,
    task_use_case=Depends(Provide[Container.task_use_case]),
):
    await task_use_case.delete_by_id(task_id)
