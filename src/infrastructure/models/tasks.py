import enum
from typing import Annotated

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.models.base import Base

# TODO change postgres enum realization


class TaskStatus(enum.Enum):
    IN_PROGRESS = "in progress"
    DONE = "done"


pg_enum = Annotated[
    str, mapped_column(PgEnum(TaskStatus), default=TaskStatus.IN_PROGRESS)
]


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = (UniqueConstraint("name", "sheet_id"),)

    name: Mapped[str] = mapped_column(String(20))
    description: Mapped[str] = mapped_column(String(100), nullable=True)
    status: Mapped[pg_enum]
    sheet_id: Mapped[int] = mapped_column(
        ForeignKey("sheets.id", ondelete="CASCADE"), nullable=False
    )
