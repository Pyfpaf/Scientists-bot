from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class TokenConfig(BaseModel):
    ai: str = None
    bot: str = None


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_BOT__",
        extra="ignore",
    )
    token: TokenConfig = TokenConfig()


settings = Settings()
