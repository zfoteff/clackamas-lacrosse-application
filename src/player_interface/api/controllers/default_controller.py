__version__ = "0.1.0"
__author__ = "Zac Foteff"

from typing import Self
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from providers.player_data_service_provider import PlayerDataServiceProvider

templates = Jinja2Templates(directory="api/templates")


class DefaultController:
    _player_data_service_provider: PlayerDataServiceProvider

    def __init__(self) -> Self:
        self._player_data_service_provider = PlayerDataServiceProvider()

    async def render_homepage(request: Request) -> HTMLResponse:
        return templates.TemplateResponse("home.html", context={"request": request})

    async def render_stats_page(request: Request) -> HTMLResponse:
        return templates.TemplateResponse(
            "statistics.html", context={"request": request}
        )

    async def render_player_page(request: Request) -> HTMLResponse:
        players = self._client.get_players_by_filters()
        return templates.TemplateResponse(
            "players.html", context={"request": request, "players": players}
        )
