from datetime import datetime

from pydantic import BaseModel, Field


class SheetIdDTO(BaseModel):
    id: int


class SheetCreateUpdateDTO(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    description: str | None = Field(max_length=100, default=None)


class SheetRetrieveDTO(SheetIdDTO, SheetCreateUpdateDTO):
    created_at: datetime
    updated_at: datetime
