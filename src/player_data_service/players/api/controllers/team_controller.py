__version__ = "0.1.0"
__author__ = "Zac Foteff"

from bin.logger import Logger
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from players.models.dto.team import Team
from players.teams_db_interface import TeamsDatabaseInterface

logger = Logger("team-controller")
db_interface = TeamsDatabaseInterface()


class TeamController:
    @classmethod
    async def create_team(team: Team) -> JSONResponse:
        return JSONResponse(
            status_code=201, content={"status": 201, "data": jsonable_encoder(team)}
        )

    @classmethod
    async def get_teams(request: Request) -> JSONResponse:
        return JSONResponse(status_code=200, content={"status": 200, "data": []})

    @classmethod
    async def update_team(team_id: str, team: Team) -> JSONResponse:
        return JSONResponse(
            status_code=201, content={"status": 201, "data": jsonable_encoder(team)}
        )

    @classmethod
    async def delete_team(team_id: str) -> JSONResponse:
        return JSONResponse(status_code=200, content={"status": 200, "data": {"team_id": team_id}})
