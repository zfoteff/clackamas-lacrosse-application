import json
from typing import Annotated, Dict, Self, Tuple

from config import cache_config
from config.cache_config import CacheConfig
from fastapi import Depends
from models.player_data_service_response import PlayerDataServiceResponse
from redis import Redis
from redis.exceptions import ConnectionError, DataError

from bin.logger import Logger

logger = Logger("cache")


class CacheClient:
    def __init__(
        self,
        config: CacheConfig = Annotated[
            cache_config.get_cache_config(), Depends(cache_config.get_cache_config())
        ],
    ) -> Self:
        self._client = Redis(
            host=config.host,
            port=config.port,
            socket_connect_timeout=config.connect_timeout,
            socket_timeout=config.read_timeout,
            health_check_interval=10,
            retry_on_timeout=False,
            socket_keepalive=True,
        )
        self._ttl = config.ttl

    def cache_response(self, url: str, response: PlayerDataServiceResponse) -> bool:
        response_bytes = json.dumps(response.data).encode("utf-8")
        try:
            self._client.set(
                name=url,
                value=response_bytes,
                ex=self._ttl,
            )
            logger.info(f"Cached value for {url}")
            return True
        except ConnectionError as e:
            logger.error(f"Connection error to cache: {e}")
            return False
        except DataError as e:
            logger.error(f"Error caching value {response.data}\n{e}")
            return False

    def retrieve_response(self, key: str) -> Tuple[bool, PlayerDataServiceResponse | None]:
        try:
            cached_response = self._client.get(key)
            if cached_response is None:
                logger.info(f"Cache miss: {key}")
                return (False, None)

            logger.info(f"Cache hit for {key}")
            return (
                True,
                PlayerDataServiceResponse(200, data=json.loads(cached_response.decode("utf-8"))),
            )
        except ConnectionError as e:
            logger.error(f"Connection error to cache: {e}")
            return (False, PlayerDataServiceResponse(500, data={"message": f"{e}"}))

    def cache_health(self) -> Dict[str, str]:
        try:
            res = self._client.ping()
            if res:
                return {"status": "UP", "response": res}
            else:
                return {"status": "DOWN", "response": res}
        except ConnectionError as e:
            return {"status": "DOWN", "error": str(e)}
