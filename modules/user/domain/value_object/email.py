"""Email value object enforces basic format invariants."""
from __future__ import annotations

import re
from dataclasses import dataclass


_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@dataclass(frozen=True)
class Email:
    value: str

    def __post_init__(self) -> None:
        if not _EMAIL_RE.match(self.value):
            raise ValueError("invalid email format")

    def __str__(self) -> str:  # pragma: no cover - convenience only
        return self.value

    def equals(self, other: "Email") -> bool:
        return self.value.lower() == other.value.lower()
