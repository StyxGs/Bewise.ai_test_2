from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.base import Base


class Record(Base):
    __tablename__ = 'records'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    identifier_uuid: Mapped[UUID] = mapped_column(UUID, nullable=False, unique=True)
    data_audio: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self) -> str:
        return f'Audio(id={self.id!r}, user_ID={self.user_id!r})'
