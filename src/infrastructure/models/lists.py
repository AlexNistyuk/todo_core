from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.models.base import Base


class List(Base):
    __tablename__ = "lists"

    name: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(60), nullable=True)
