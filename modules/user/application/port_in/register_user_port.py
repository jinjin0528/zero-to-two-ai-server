"""Input port for registering a user."""
from abc import ABC, abstractmethod
from modules.user.application.dto.user_dto import RegisterUserCommand, UserDTO


class RegisterUserUseCase(ABC):
    @abstractmethod
    def execute(self, command: RegisterUserCommand) -> UserDTO:
        """Registers a user and returns the created user DTO."""
        raise NotImplementedError
