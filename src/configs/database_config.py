from pydantic import BaseModel, Field, SecretStr


class DatabaseConfig(BaseModel):
    driver: str = Field(description="Database driver")
    host: str = Field(description="Database host")
    port: int = Field(description="Database port")
    username: str = Field(description="Database username")
    password: SecretStr = Field(description="Database password")
    database: str = Field(description="Database schema")
    sslmode: str = Field(description="Database SSL mode")
