from datetime import datetime

from pydantic import BaseModel, Field

from domain.enums.tasks import TaskStatus


class TaskIdDTO(BaseModel):
    id: int


class TaskCreateDTO(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    description: str | None = Field(max_length=100, default=None)
    sheet_id: int


class TaskUpdateDTO(TaskCreateDTO):
    status: TaskStatus


class TaskRetrieveDTO(TaskIdDTO, TaskUpdateDTO):
    created_at: datetime
    updated_at: datetime
