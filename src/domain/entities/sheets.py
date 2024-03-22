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
    creator_id: int
    task_count: int | None = None
    status_count: int | None = None

    class Config:
        from_attributes = True

    @classmethod
    def model_validation(cls, *args, **kwargs):
        task_count = kwargs.pop("task_count", None)
        status_count = kwargs.pop("status_count", None)

        obj = cls.model_validate(*args, **kwargs)
        obj.task_count = task_count
        obj.status_count = status_count

        return obj
