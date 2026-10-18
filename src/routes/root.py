from fastapi import APIRouter

router_router = APIRouter()


@router_router.get("/")
def root() -> dict:
    return {"message": "Hello World"}
