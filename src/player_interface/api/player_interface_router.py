from api.controllers.default_controller import DefaultController
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

PLAYER_INTERFACE_ROUTER = APIRouter()


PLAYER_INTERFACE_ROUTER.add_api_route(
    path="/",
    endpoint=DefaultController.render_homepage,
    description="Render application homepage",
    methods=["GET"],
    response_class=HTMLResponse,
)

PLAYER_INTERFACE_ROUTER.add_api_route(
    path="/players",
    endpoint=DefaultController.render_players_page,
    description="Render players page",
    methods=["GET"],
    response_class=HTMLResponse,
)

PLAYER_INTERFACE_ROUTER.add_api_route(
    path="/players/{player_id}",
    endpoint=DefaultController.render_player_page,
    description="Render player page with statistics",
    methods=["GET"],
    response_class=HTMLResponse,
)

PLAYER_INTERFACE_ROUTER.add_api_route(
    path="/teams",
    endpoint=DefaultController.render_teams_page,
    description="Render teams page",
    methods=["GET"],
    response_class=HTMLResponse,
)

PLAYER_INTERFACE_ROUTER.add_api_route(
    path="/games",
    endpoint=DefaultController.render_game_page,
    description="Render games page",
    methods=["GET"],
    response_class=HTMLResponse,
)
