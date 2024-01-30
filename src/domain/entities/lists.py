from datetime import datetime

from pydantic import BaseModel, Field


class ListIdDTO(BaseModel):
    id: int


class ListCreateUpdateDTO(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    description: str = Field(max_length=100)


class ListRetrieveDTO(ListIdDTO, ListCreateUpdateDTO):
    created_at: datetime
    updated_at: datetime
