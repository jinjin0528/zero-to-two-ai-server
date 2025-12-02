"""Web adapter example. Replace with real framework (e.g., FastAPI/Flask) when wiring."""
from __future__ import annotations

from modules.user.application.dto.user_dto import RegisterUserCommand
from modules.user.application.port_in.register_user_port import RegisterUserUseCase


def register_user_handler(payload: dict, usecase: RegisterUserUseCase):
    """Minimal framework-agnostic handler example."""
    command = RegisterUserCommand(email=payload["email"], name=payload["name"])
    return usecase.execute(command)
