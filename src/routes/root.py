from fastapi import APIRouter


def create_root_router() -> APIRouter:
    router_router = APIRouter()

    @router_router.get("/")
    def root() -> dict:
        return {"message": "Hello World"}

    return router_router
