from fastapi import FastAPI

from routes.routes import create_routes


def register_routers(app: FastAPI) -> None:
    for router in create_routes():
        app.include_router(router)


def create_app() -> FastAPI:
    app = FastAPI(
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
    )
    register_routers(app)
    return app
