from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.models.base import Base
from infrastructure.models.mixins import TimeMixin


class Sheet(Base, TimeMixin):
    __tablename__ = "sheets"

    name: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[str] = mapped_column(String(60), nullable=True)
    creator_id: Mapped[int] = mapped_column(nullable=False)
