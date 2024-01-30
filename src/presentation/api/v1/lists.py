from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from application.use_cases.lists import ListUseCase
from domain.entities.lists import ListCreateUpdateDTO, ListIdDTO, ListRetrieveDTO

router = APIRouter()


@router.get("/", response_model=list[ListRetrieveDTO], status_code=HTTP_200_OK)
async def get_all_lists():
    return await ListUseCase().get_all()


@router.post("/", response_model=ListIdDTO, status_code=HTTP_201_CREATED)
async def create_list(new_list: ListCreateUpdateDTO):
    list_id = await ListUseCase().insert(new_list.model_dump())

    return {"id": list_id}


@router.get("/{list_id}", response_model=ListRetrieveDTO, status_code=HTTP_200_OK)
async def get_list_by_id(list_id: int):
    return await ListUseCase().get_by_id(list_id)


@router.put("/{list_id}", status_code=HTTP_200_OK)
async def update_list_by_id(list_id: int, updated_list: ListCreateUpdateDTO):
    return await ListUseCase().update_by_id(updated_list.model_dump(), list_id)


@router.delete("/{list_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_list_by_id(list_id: int):
    return await ListUseCase().delete_by_id(list_id)
