#!/usr/bin/env python
__author__ = "Zac Foteff"
__version__ = "0.1.0"

import argparse
from contextlib import asynccontextmanager

from api.player_interface_router import PLAYER_INTERFACE_ROUTER
from fastapi import APIRouter, FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from bin.logger import Logger

logger = Logger("player-interface")

FAVICON_PATH = "static/favicon.ico"


async def get_health() -> JSONResponse:
    """Healthcheck for the Player Interface service. Asserts the service is running and has
    connection to the Player Data Service

    Returns:
        JSONResponse: Healthcheck response
    """
    return JSONResponse(status_code=200, content={"status": 200, "response": "Running"})


async def get_favicon():
    return FileResponse(FAVICON_PATH)


default_router = APIRouter()
default_router.add_api_route(
    "/health",
    get_health,
    description="Healthcheck endpoint for the Player Data Service",
    methods=["GET"],
    tags=["default"],
    responses={
        200: {
            "description": "Service is running as expected",
            "content": {
                "application/json": {
                    "example": [{"status": 200, "response": "Running"}],
                }
            },
        }
    },
)
default_router.add_api_route(
    path="/favicon.ico",
    endpoint=get_favicon,
    description="Retrieve favicon",
    methods=["GET"],
    response_class=FileResponse,
    include_in_schema=False,
)


@asynccontextmanager
async def lifespan(api: FastAPI):
    # Startup events
    api.include_router(default_router)
    api.include_router(PLAYER_INTERFACE_ROUTER)
    yield
    # Shutdown events


app = FastAPI(
    title="Player Interface",
    description="Player Interface for the APPNAME",
    lifespan=lifespan,
    version=__version__,
    license_info={"name": "MIT", "url": "https://opensource.org/license/mit"},
)
app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    from uvicorn import run

    parser = argparse.ArgumentParser(
        description="""
        Front end for the Bardown application. Interfaces with the Player
        Data Service to display information to the user. Run with no arguments
        to start API for CRUD operations
    """
    )
    parser.add_argument(
        "-v",
        "--version",
        help="Display the version of the service",
        action="store_true",
    )
    args = parser.parse_args()

    if args.version is True:
        print(app.version)
    else:
        run(
            app="player_interface:app",
            log_level="debug",
            host="0.0.0.0",
            port=3000,
            reload=True,
        )
