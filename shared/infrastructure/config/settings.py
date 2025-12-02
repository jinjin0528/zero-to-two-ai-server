"""Infrastructure settings placeholder (e.g., env parsing)."""
import os


class Settings:
    def __init__(self):
        self.env = os.environ.get("APP_ENV", "local")


def load_settings() -> Settings:
    return Settings()
