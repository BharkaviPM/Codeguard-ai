from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "CodeGuard AI v2"

    DEBUG: bool = True

    DATABASE_URL: str

    UPLOAD_DIR: str = "uploads"

    WORKSPACE_DIR: str = "workspace"

    REPORT_DIR: str = "reports"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()