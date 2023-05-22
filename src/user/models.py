import uuid

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.base import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(String(100), nullable=False)
    token: Mapped[UUID] = mapped_column(UUID, nullable=False, unique=True, default=uuid.uuid4)

    def __repr__(self) -> str:
        return f'User(id={self.id!r}, username={self.username!r})'
