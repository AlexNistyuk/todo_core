from datetime import datetime

from pydantic import BaseModel, Field

from domain.entities.sheets import SheetRetrieveDTO
from domain.entities.statuses import StatusRetrieveDTO


class TaskIdDTO(BaseModel):
    id: int


class TaskUpdateStatusDTO(BaseModel):
    status_id: int


class TaskCreateUpdateDTO(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    description: str | None = Field(max_length=100, default=None)
    estimated_date: datetime | None
    assignee: str | None = Field(max_length=20, default=None)


class TaskUpdateDTO(TaskCreateUpdateDTO, TaskUpdateStatusDTO):
    status_id: int


class TaskCreateDTO(TaskCreateUpdateDTO):
    sheet_id: int


class TaskRetrieveDTO(TaskIdDTO, TaskCreateDTO):
    status_id: int
    created_at: datetime
    updated_at: datetime
    sheet: SheetRetrieveDTO | None = None
    status: StatusRetrieveDTO | None = None
