from typing import Dict

from fastapi import APIRouter

from controllers.root_controller import index


def create_root_router() -> APIRouter:
    router_router = APIRouter()

    @router_router.get("/")
    async def root() -> Dict[str, str]:
        return await index()

    return router_router
