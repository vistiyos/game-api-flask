from dataclasses import dataclass

from sqlalchemy.orm import Mapped, mapped_column
from src.infrastructure.db import db


@dataclass
class Game(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
