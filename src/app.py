from fastapi import FastAPI

from routes.routes import create_routes


def create_app() -> FastAPI:
    app = FastAPI(
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
    )

    app.include_router(create_routes(config_registry))

    return app
