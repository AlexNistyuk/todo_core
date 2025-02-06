from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.models.base import Base


class Status(Base):
    __tablename__ = "statuses"
    __table_args__ = (UniqueConstraint("name", "sheet_id"),)

    name: Mapped[str] = mapped_column(String(20), nullable=False)
    sheet_id: Mapped[int] = mapped_column(ForeignKey("sheets.id", ondelete="CASCADE"))
