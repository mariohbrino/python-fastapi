from typing import List

from fastapi import APIRouter

from routes.root_router import create_root_router

index_router: List[APIRouter] = [
    create_root_router(),
]
