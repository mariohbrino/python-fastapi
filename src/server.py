from typing import Dict

from fastapi import FastAPI

app_configs: Dict[str, None] = {
    "docs_url": None,
    "redoc_url": None,
    "openapi_url": None,
}


app = FastAPI(
    **app_configs,
)


@app.get("/")
def home() -> Dict[str, str]:
    return {"message": "Hello World"}
