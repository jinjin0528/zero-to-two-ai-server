"""Application entrypoint for DI/bootstrap and router wiring."""
from modules.user.adapter.input.web.router.user_router import register_user_handler
from modules.user.adapter.output.in_memory_user_repository import InMemoryUserRepository
from modules.user.application.usecase.register_user import RegisterUserService
from shared.infrastructure.config.settings import load_settings


def bootstrap():
    settings = load_settings()
    user_repository = InMemoryUserRepository()
    register_user_usecase = RegisterUserService(user_repository)
    container = {
        "settings": settings,
        "register_user_usecase": register_user_usecase,
    }
    return container


def main() -> None:
    container = bootstrap()
    result = register_user_handler(
        {"email": "demo@example.com", "name": "Demo User"},
        container["register_user_usecase"],
    )
    print(result)


if __name__ == "__main__":
    main()
