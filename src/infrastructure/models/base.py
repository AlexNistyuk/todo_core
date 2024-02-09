from sqlalchemy import Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from domain.utils.task_status import TaskStatus


class Base(DeclarativeBase):
    type_annotation_map = {TaskStatus: Enum(TaskStatus)}
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
