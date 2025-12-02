"""Domain entity definitions (pure, without external dependencies)."""
from dataclasses import dataclass
from modules.user.domain.value_object.email import Email


@dataclass(frozen=True)
class User:
    id: str
    email: Email
    name: str

    def rename(self, new_name: str) -> "User":
        cleaned = new_name.strip()
        if not cleaned:
            raise ValueError("user name must not be blank")
        return User(id=self.id, email=self.email, name=cleaned)
