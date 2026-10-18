from fastapi import FastAPI

from routes.root_router import create_root_router


def create_app() -> FastAPI:
    app = FastAPI(
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
    )
    app.include_router(create_root_router())
    return app
