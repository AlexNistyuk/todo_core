from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from domain.utils.task_status import TaskStatus
from infrastructure.models.base import Base
from infrastructure.models.mixins import TimeMixin


class Task(Base, TimeMixin):
    __tablename__ = "tasks"
    __table_args__ = (UniqueConstraint("name", "sheet_id"),)

    name: Mapped[str] = mapped_column(String(20))
    description: Mapped[str] = mapped_column(String(100), nullable=True)
    status: Mapped[TaskStatus] = mapped_column(
        server_default=TaskStatus.in_progress.value
    )
    sheet_id: Mapped[int] = mapped_column(
        ForeignKey("sheets.id", ondelete="CASCADE"), nullable=False
    )
