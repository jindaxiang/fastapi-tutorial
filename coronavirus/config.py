from pydantic import BaseSettings

from functools import lru_cache


class LocalSettings(BaseSettings):
    """
    本地配置文件类
    """

    env_name: str = "Local Settings"
    db_url: str = "mysql+pymysql://root:king@localhost/aktest?charset=utf8mb4"

    class Config:
        env_file = ".env"


@lru_cache()
def get_local_settings():
    """
    获取本地配置文件
    """
    local_settings = LocalSettings()
    print(f"加载本地配置文件：{local_settings.env_name}")
    return local_settings
