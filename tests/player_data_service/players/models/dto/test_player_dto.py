import pytest

from src.logger import Logger
from src.player_data_service.players.models.dto.player import Player
from tests.bin.decorators.timed import timed
from tests.constants import VALID_PLAYER

logger = Logger("test")


@timed(logger)
def test_create_single_player_dto_instance() -> None:
    player = Player(
        number=VALID_PLAYER["number"],
        first_name=VALID_PLAYER["first_name"],
        last_name=VALID_PLAYER["last_name"],
        position=VALID_PLAYER["position"],
        grade=VALID_PLAYER["grade"],
        school=VALID_PLAYER["school"],
    )
    logger.debug(player)
    assert player is not None