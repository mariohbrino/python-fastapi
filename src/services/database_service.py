from contextlib import contextmanager
from typing import Any, Generator, Mapping

from sqlalchemy import Connection, Engine, create_engine, text
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session, sessionmaker

from configs.database_config import DatabaseConfig

DRIVERS_MAP: dict[str, str] = {
    "pgsql": "postgresql+psycopg2",
}


class DatabaseService:
    def __init__(self, config: DatabaseConfig) -> None:
        self._engine: Engine = create_engine(
            self._create_url(config),
            pool_pre_ping=True,  # detect dead connections before using them
            pool_size=5,
            max_overflow=10,
        )
        self._session_factory: sessionmaker[Session] = sessionmaker(
            self._engine,
            expire_on_commit=False,
        )

    @staticmethod
    def _create_url(config: DatabaseConfig) -> URL:
        if config.driver not in DRIVERS_MAP:
            raise ValueError(f"Unsupported database driver: {config.driver}")

        return URL.create(
            drivername=DRIVERS_MAP[config.driver],
            username=config.username,
            password=config.password.get_secret_value(),
            host=config.host,
            port=config.port,
            database=config.database,
            query={"sslmode": config.sslmode},
        )

    @property
    def engine(self) -> Engine:
        return self._engine

    @contextmanager
    def session(self) -> Generator[Session, None, None]:
        """ORM unit of work: commits on success, rolls back on error."""
        with self._session_factory.begin() as session:
            yield session

    @contextmanager
    def connection(self) -> Generator[Connection, None, None]:
        """Core-level connection in a transaction: commits on success, rolls back on error."""
        with self._engine.begin() as conn:
            yield conn

    def execute_raw(
        self,
        sql: str,
        params: Mapping[str, Any] | None = None,
    ) -> list[dict]:
        """One-off raw query. Returns rows as dicts."""
        with self.connection() as conn:
            result = conn.execute(text(sql), params or {})
            return [dict(row) for row in result.mappings()] if result.returns_rows else []

    def dispose(self) -> None:
        """Close all pooled connections. Call on application shutdown."""
        self._engine.dispose()
