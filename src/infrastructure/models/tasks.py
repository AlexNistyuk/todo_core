from datetime import datetime

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.models.base import Base
from infrastructure.models.mixins import TimeMixin
from infrastructure.models.sheets import Sheet
from infrastructure.models.statuses import Status


class Task(Base, TimeMixin):
    __tablename__ = "tasks"
    __table_args__ = (UniqueConstraint("name", "sheet_id"),)

    name: Mapped[str] = mapped_column(String(20))
    description: Mapped[str] = mapped_column(String(100), nullable=True)
    status_id: Mapped[int] = mapped_column(ForeignKey("statuses.id"))
    sheet_id: Mapped[int] = mapped_column(
        ForeignKey("sheets.id", ondelete="CASCADE"), nullable=False
    )
    assignee: Mapped[str] = mapped_column(String(20), nullable=True)
    estimated_date: Mapped[datetime] = mapped_column(nullable=True)


class TaskRelationship(Task):
    sheet: Mapped["Sheet"] = relationship()
    status: Mapped["Status"] = relationship()
