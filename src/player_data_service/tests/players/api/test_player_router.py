__version__ = "1.0.0"
__author__ = "Zac Foteff"


from bin.logger import Logger
from tests.bin.decorators.timed import timed

logger = Logger("test")


@timed(logger)
def test_get_health_endpoint() -> None:
    pass
