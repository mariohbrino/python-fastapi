from fastapi import FastAPI

from routes.index_router import index_router


def register_routers(app: FastAPI) -> None:
    for router in index_router:
        app.include_router(router)


def create_app() -> FastAPI:
    app = FastAPI(
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
    )
    register_routers(app)
    return app
