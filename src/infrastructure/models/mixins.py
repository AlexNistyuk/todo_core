from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column


class TimeMixin:
    """Add created_at and updated_at fields"""

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
