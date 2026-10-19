from fastapi import APIRouter

from routes.root_router import create_root_router


def create_routes() -> APIRouter:
    router = APIRouter()
    router.include_router(create_root_router())
    return router
