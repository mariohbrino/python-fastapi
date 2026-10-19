import pytest
from pydantic import ValidationError

from configs.database_config import DatabaseConfig
from container import AppContainer
from services.database_service import DatabaseService

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


def test_database_service_builds_engine_from_config() -> None:
    database: DatabaseConfig = make_container().config_registry().database
    service = DatabaseService(database)
    assert service.engine.url.render_as_string(hide_password=False) == (
        "postgresql+psycopg2://user:secret@localhost:5432/app?sslmode=allow"
    )
    service.dispose()
