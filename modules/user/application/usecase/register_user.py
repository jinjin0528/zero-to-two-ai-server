"""Register user use case implementation."""
from __future__ import annotations

import uuid
from modules.user.application.dto.user_dto import RegisterUserCommand, UserDTO
from modules.user.application.port_in.register_user_port import RegisterUserUseCase
from modules.user.application.port_out.user_repository import UserRepository
from modules.user.domain.user_data import User
from modules.user.domain.value_object.email import Email


class RegisterUserService(RegisterUserUseCase):
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def execute(self, command: RegisterUserCommand) -> UserDTO:
        email_vo = Email(command.email)
        if self._user_repository.find_by_email(email_vo.value):
            raise ValueError("email already registered")

        user = User(id=str(uuid.uuid4()), email=email_vo, name=command.name.strip())
        saved = self._user_repository.save(user)
        return UserDTO.from_entity(saved)
