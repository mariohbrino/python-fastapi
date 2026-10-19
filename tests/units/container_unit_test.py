import pytest
from pydantic import ValidationError

from configs.database_config import DatabaseConfig
from container import AppContainer

DATABASE = {
    "driver": "pgsql",
    "host": "localhost",
    "port": "5432",
    "database": "app",
    "username": "user",
    "password": "secret",
    "sslmode": "allow",
}


def make_container() -> AppContainer:
    container = AppContainer()
    container.config.from_dict({"database": DATABASE})
    return container


def test_config_registry_is_typed_and_hides_password() -> None:
    database: DatabaseConfig = make_container().config_registry().database
    assert database.port == 5432
    assert database.password.get_secret_value() == "secret"
    assert "secret" not in repr(database)


def test_config_registry_rejects_invalid_config() -> None:
    container: AppContainer = make_container()
    container.config.from_dict({"database": {**DATABASE, "port": "not-a-port"}})
    with pytest.raises(ValidationError):
        container.config_registry()
