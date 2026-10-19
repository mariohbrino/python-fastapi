from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter

from config import ConfigRegistry
from container import AppContainer
from controllers.root_controller import index


@inject
def create_root_router(
    config_registry: ConfigRegistry = Provide[AppContainer.config_registry],
) -> APIRouter:
    root_router = APIRouter()

    @root_router.get("/")
    async def root() -> dict[str, str]:
        return await index()

    return root_router
