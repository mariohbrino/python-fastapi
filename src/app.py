from typing import Dict

from fastapi import FastAPI

from routes.root import create_root_router


def create_app() -> FastAPI:
    app_configs: Dict[str, None] = {
        "docs_url": None,
        "redoc_url": None,
        "openapi_url": None,
    }
    app = FastAPI(
        **app_configs,
    )
    app.include_router(create_root_router())
    return app
