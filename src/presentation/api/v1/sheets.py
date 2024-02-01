from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from application.use_cases.sheets import SheetUseCase
from domain.entities.sheets import SheetCreateUpdateDTO, SheetIdDTO, SheetRetrieveDTO
from infrastructure.permissions.users import IsAdmin

router = APIRouter()


@router.get("/", response_model=list[SheetRetrieveDTO], status_code=HTTP_200_OK)
async def get_all_sheets():
    return await SheetUseCase().get_all()


@router.post("/", response_model=SheetIdDTO, status_code=HTTP_201_CREATED)
async def create_sheet(new_sheet: SheetCreateUpdateDTO, permission=Depends(IsAdmin())):
    sheet_id = await SheetUseCase().insert(new_sheet.model_dump())

    return {"id": sheet_id}


@router.get("/{sheet_id}", response_model=SheetRetrieveDTO, status_code=HTTP_200_OK)
async def get_sheet_by_id(sheet_id: int):
    return await SheetUseCase().get_by_id(sheet_id)


@router.put("/{sheet_id}", status_code=HTTP_200_OK)
async def update_sheet_by_id(
    sheet_id: int, updated_sheet: SheetCreateUpdateDTO, permission=Depends(IsAdmin())
):
    return await SheetUseCase().update_by_id(updated_sheet.model_dump(), sheet_id)


@router.delete("/{sheet_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_sheet_by_id(sheet_id: int, permission=Depends(IsAdmin())):
    return await SheetUseCase().delete_by_id(sheet_id)
