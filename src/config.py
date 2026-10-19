from pydantic import BaseModel

from configs.database_config import DatabaseConfig


class ConfigRegistry(BaseModel):
    database: DatabaseConfig
