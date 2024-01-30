from datetime import datetime

from pydantic import BaseModel, Field


class TaskIdDTO(BaseModel):
    id: int


class TaskCreateDTO(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    description: str = Field(max_length=100)
    list_id: int


class TaskUpdateDTO(TaskCreateDTO):
    status: str


class TaskRetrieveDTO(TaskIdDTO, TaskUpdateDTO):
    created_at: datetime
    updated_at: datetime
