from typing import List

from fastapi import APIRouter

from routes.root_router import create_root_router


def create_routes() -> List[APIRouter]:
    return [
        create_root_router(),
    ]
