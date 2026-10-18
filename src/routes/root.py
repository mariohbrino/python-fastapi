from fastapi import APIRouter

router_router = APIRouter()


@router_router.get("/")
def home() -> dict:
    return {"message": "Hello World"}
