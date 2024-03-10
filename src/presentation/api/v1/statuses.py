from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_503_SERVICE_UNAVAILABLE,
)

from application.dependencies import Container
from domain.entities.statuses import StatusCreateDTO, StatusRetrieveDTO, StatusUpdateDTO

router = APIRouter()


@router.get(
    "/",
    response_model=list[StatusRetrieveDTO],
    status_code=HTTP_200_OK,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
@inject
async def get_all_statuses(
    sheet_id: int = None, status_use_case=Depends(Provide[Container.status_use_case])
):
    if sheet_id is None:
        return await status_use_case.get_all()
    return await status_use_case.get_by_sheet_id(sheet_id)


@router.post(
    "/",
    status_code=HTTP_201_CREATED,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
@inject
async def create_statuses(
    new_statuses: StatusCreateDTO,
    status_use_case=Depends(Provide[Container.status_use_case]),
):
    await status_use_case.insert(new_statuses.model_dump())


@router.get(
    "/{status_id}/",
    response_model=StatusRetrieveDTO,
    status_code=HTTP_200_OK,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
@inject
async def get_status_by_id(
    status_id: int,
    status_use_case=Depends(Provide[Container.status_use_case]),
):
    return await status_use_case.get_by_id(status_id)


@router.put(
    "/{status_id}/",
    status_code=HTTP_204_NO_CONTENT,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
@inject
async def update_status_by_id(
    status_id: int,
    updated_status: StatusUpdateDTO,
    status_use_case=Depends(Provide[Container.status_use_case]),
):
    return await status_use_case.update_by_id(updated_status.model_dump(), status_id)


@router.delete(
    "/{status_id}/",
    status_code=HTTP_204_NO_CONTENT,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
@inject
async def delete_status_by_id(
    status_id: int,
    status_use_case=Depends(Provide[Container.status_use_case]),
):
    await status_use_case.delete_by_id(status_id)
