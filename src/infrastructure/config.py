import os
from functools import lru_cache
from pathlib import Path

from pydantic import Extra
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

    model_config = SettingsConfigDict(env_file=ENV_FILE_PATH, extra=Extra.allow)


@lru_cache
def get_settings():
    return Settings()
