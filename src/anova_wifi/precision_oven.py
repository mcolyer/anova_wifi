import aiohttp


class AnovaPrecisionOven:
    def __init__(
        self, session: aiohttp.ClientSession, device_key: str, type: str, jwt: str
    ) -> None:
        self.session = session
        self.device_key = device_key
        self.type = type
        self._jwt = jwt
