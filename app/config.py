from functools import lru_cache

from decouple import config
from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Extend from BaseSetting, all the configuration overall
    fastapi sets in this class
    """

    model_config = ConfigDict(protected_namespaces=("settings_",))

    service_name: str = config("SERVICE_NAME")  # read from .env file
    secret_key: str = config("SECRET_KEY")  # read from .env file
    # The list of origins allowed to communicate with
    allow_origins: list = ["*"]
    # Allows cookies to be supported for cross-origin requests
    allow_credentials: bool = True
    # Allows a list of http methods to for cross-origin requests
    allow_methods: list = ["*"]
    # Allows a list of http headers to for cross-origin requests
    allow_headers: list = ["*"]

    # model configs
    model_path: str = "en_core_web_sm"


@lru_cache()
def get_settings():
    """
    Once the Setting object created , it returns same cached object
    :return: Settings
    """
    return Settings()