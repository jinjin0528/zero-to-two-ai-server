"""Output port for user persistence."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional
from modules.user.domain.user_data import User


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        raise NotImplementedError
