from tests.bin.decorators.timed import timed

from bin.logger import Logger

logger = Logger("test")


@timed(logger)
def test_get_health_endpoint() -> None:
    pass
