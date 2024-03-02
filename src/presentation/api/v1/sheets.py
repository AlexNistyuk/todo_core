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
from domain.entities.sheets import SheetCreateUpdateDTO, SheetIdDTO, SheetRetrieveDTO

router = APIRouter()


@router.get(
    "/",
    response_model=list[SheetRetrieveDTO],
    status_code=HTTP_200_OK,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
@inject
async def get_all_sheets(sheet_use_case=Depends(Provide[Container.sheet_use_case])):
    return await sheet_use_case.get_all()


@router.post(
    "/",
    response_model=SheetIdDTO,
    status_code=HTTP_201_CREATED,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
@inject
async def create_sheet(
    request: Request,
    new_sheet: SheetCreateUpdateDTO,
    sheet_use_case=Depends(Provide[Container.sheet_use_case]),
):
    return await sheet_use_case.insert(new_sheet.model_dump(), request.state.user)


@router.get(
    "/{sheet_id}/",
    response_model=SheetRetrieveDTO,
    status_code=HTTP_200_OK,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
@inject
async def get_sheet_by_id(
    request: Request,
    sheet_id: int,
    sheet_use_case=Depends(Provide[Container.sheet_use_case]),
):
    return await sheet_use_case.get_by_id(sheet_id, request.state.user)


@router.put(
    "/{sheet_id}/",
    status_code=HTTP_204_NO_CONTENT,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
@inject
async def update_sheet_by_id(
    sheet_id: int,
    updated_sheet: SheetCreateUpdateDTO,
    sheet_use_case=Depends(Provide[Container.sheet_use_case]),
):
    await sheet_use_case.update_by_id(updated_sheet.model_dump(), sheet_id)


@router.delete(
    "/{sheet_id}/",
    status_code=HTTP_204_NO_CONTENT,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
@inject
async def delete_sheet_by_id(
    sheet_id: int,
    sheet_use_case=Depends(Provide[Container.sheet_use_case]),
):
    await sheet_use_case.delete_by_id(sheet_id)
