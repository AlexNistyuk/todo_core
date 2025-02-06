import os
from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE_PATH = os.path.join(BASE_DIR.parent.parent, ".env")


class Settings(BaseSettings):
    db_url: str
    db_pool_size: int
    db_max_overflow: int
    user_info_url: str
    kafka_url: str
    kafka_topic: str
    allow_origins: list
    allow_methods: list
    allow_headers: list
    allow_credentials: bool
    default_task_statuses: list

    model_config = SettingsConfigDict(env_file=ENV_FILE_PATH, extra="allow")


@lru_cache
def get_settings():
    return Settings()
