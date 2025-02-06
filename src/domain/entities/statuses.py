from pydantic import BaseModel, Field


class StatusUpdateDTO(BaseModel):
    name: str = Field(max_length=20, min_length=1)


class StatusCreateDTO(BaseModel):
    names: list[str]
    sheet_id: int


class StatusRetrieveDTO(StatusUpdateDTO):
    sheet_id: int
    id: int
