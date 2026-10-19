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


def test_database_service_builds_engine_from_config() -> None:
    database: DatabaseConfig = make_container().config_registry().database
    service = DatabaseService(database)
    assert service.engine.url.render_as_string(hide_password=False) == (
        "postgresql+psycopg2://user:secret@localhost:5432/app?sslmode=allow"
    )
    service.dispose()
