from fastapi import FastAPI

from container import AppContainer
from routes.routes import create_routes


def create_app() -> FastAPI:
    AppContainer()

    app = FastAPI(
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
    )

    app.include_router(create_routes())

    return app
