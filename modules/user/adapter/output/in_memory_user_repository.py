"""In-memory adapter implementing the UserRepository output port."""
from __future__ import annotations

from typing import Dict, Optional
from modules.user.application.port_out.user_repository import UserRepository
from modules.user.domain.user_data import User


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._users_by_email: Dict[str, User] = {}

    def save(self, user: User) -> User:
        self._users_by_email[user.email.value.lower()] = user
        return user

    def find_by_email(self, email: str) -> Optional[User]:
        return self._users_by_email.get(email.lower())
