#!/usr/bin/env python
__author__ = "Zac Foteff"
__version__ = "0.1.0"

import argparse
import time
from contextlib import asynccontextmanager
from logging import Logger

from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse
from games.api.games_router import GAMES_ROUTER
from players.api.player_router import PLAYER_ROUTER
from stats.api.statistics_router import STATISTICS_ROUTER
from teams.api.teams_router import TEAMS_ROUTER

from bin.metadata import servers, tags_metadata

logger = Logger("player-data-service")


async def get_health() -> JSONResponse:
    """Healthcheck for the Player data service. Asserts the service is running and has
    connection to database

    Returns:
        JSONResponse: Healthcheck response
    """
    return JSONResponse(status_code=200, content={"status": 200, "response": "Running"})


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
                    "example": [
                        {
                            "status": "UP",
                            "version": __version__,
                            "timestamp": time.time(),
                        }
                    ],
                }
            },
        }
    },
)


@asynccontextmanager
async def lifespan(api: FastAPI):
    # Startup events
    api.include_router(default_router)
    api.include_router(PLAYER_ROUTER)
    api.include_router(STATISTICS_ROUTER)
    api.include_router(GAMES_ROUTER)
    api.include_router(TEAMS_ROUTER)
    yield
    # Shutdown events


app = FastAPI(
    title="Player Data Service",
    description="Interface for player data for the Bardown application",
    lifespan=lifespan,
    version=__version__,
    license_info={"name": "MIT", "url": "https://opensource.org/license/mit"},
    openapi_tags=tags_metadata,
    servers=servers,
)

if __name__ == "__main__":
    from uvicorn import run

    parser = argparse.ArgumentParser(
        description="""
        Data interface for the Bardown application. Run with no arguments to start API for CRUD operations
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
            app="player_data_service:app",
            log_level="debug",
            host="0.0.0.0",
            port=3001,
            reload=True,
        )
