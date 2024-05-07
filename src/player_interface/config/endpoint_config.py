class EndpointConfig:
    _base_url: str
    _base_path: str
    _api_version: str
    _app_pathname: str
    _connect_timeout_ms: int
    _read_timeout_ms: int

    def __init__(
        self,
        base_url: str = "",
        base_path: str = "",
        api_version: str = "",
        app_pathname: str = "",
        connect_timeout_ms: int = 500,
        read_timeout_ms: int = 500,
    ) -> None:
        self._base_url = base_url
        self._base_path = base_path
        self._api_version = api_version
        self._app_pathname = app_pathname
        self._connect_timeout_ms = connect_timeout_ms
        self._read_timeout_ms = read_timeout_ms

    @property
    def base_url(self) -> str:
        return self._base_url

    @base_url.setter
    def base_url(self, new_base_url: str) -> None:
        self._base_url = new_base_url

    @property
    def base_path(self) -> str:
        return self._base_path

    @base_path.setter
    def base_path(self, new_base_path: str) -> None:
        self._base_path = new_base_path

    @property
    def api_version(self) -> str:
        return self._api_version

    @api_version.setter
    def api_version(self, new_api_version: str) -> None:
        self._base_path = new_api_version
