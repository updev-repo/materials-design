from urllib.parse import quote_plus

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mongodb_host: str = "localhost"
    mongodb_port: int = 27017
    mongodb_username: str | None = None
    mongodb_password: str | None = None
    mongodb_db_name: str = "materials_design"

    @property
    def mongodb_url(self) -> str:
        """Build MongoDB connection URL with optional auth."""
        if self.mongodb_username and self.mongodb_password:
            user = quote_plus(self.mongodb_username)
            password = quote_plus(self.mongodb_password)
            return f"mongodb://{user}:{password}@{self.mongodb_host}:{self.mongodb_port}"
        return f"mongodb://{self.mongodb_host}:{self.mongodb_port}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
