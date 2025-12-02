"""DTO definitions for user module."""
from dataclasses import dataclass


@dataclass
class RegisterUserCommand:
    email: str
    name: str


@dataclass
class UserDTO:
    id: str
    email: str
    name: str

    @classmethod
    def from_entity(cls, user) -> "UserDTO":
        return cls(id=user.id, email=str(user.email), name=user.name)
