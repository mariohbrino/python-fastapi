from fastapi import APIRouter

from controllers.root_controller import index


def create_root_router() -> APIRouter:
    root_router = APIRouter()

    @root_router.get("/")
    async def root() -> dict[str, str]:
        return await index()

    return root_router
