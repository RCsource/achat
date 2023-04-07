import json
import enum
from typing import TypedDict, NamedTuple
import aiohttp

from .errors import HistoryException, SonicAuthError, AchcatException

API_VERSION = 2

ASK_URL = f"https://api.writesonic.com/v{API_VERSION}/business/content/chatsonic"


class EngineType(enum.StrEnum):
    PREMIUM = "premium"


class HistoryObject(TypedDict):
    message: str
    is_sent: bool


class SonicResponse(NamedTuple):
    message: str
    image_urls: list[str]


class SonicChat:
    def __init__(
        self,
        token: str,
        enable_memory: bool = True,
        enable_google: bool = False,
        language: str = "en",
        engine: EngineType = EngineType.PREMIUM,
    ):
        self.google_enabled = enable_google
        self.language = language
        self.engine = EngineType.PREMIUM
        self.engine = engine
        self.token = token
        self.memory_enabled = enable_memory
        self._history: list[HistoryObject] = []
        self._session: aiohttp.ClientSession | None = None

    async def clear_history(self):
        if not self.memory_enabled:
            raise HistoryException("history is not enabled")
        self._history.clear()

    async def start(self):
        self._session = aiohttp.ClientSession(
            headers={
                "accept": "application/json",
                "content-type": "application/json",
                "x-api-key": self.token,
            }
        )

    async def ask(
        self,
        question: str,
    ):
        payload = {
            "enable_google_results": self.google_enabled,
            "enable_memory": self.memory_enabled,
            "input_text": question,
            "history_data": self._history,
        }

        params = {"engine": self.engine, "language": self.language}
        async with self._session.post(
            ASK_URL, params=params, data=json.dumps(payload)
        ) as response:
            if response.status == 401:
                raise SonicAuthError("wrong api token")
            if response.status == 200:
                data = await response.json()
                response = SonicResponse(**data)
                if self.memory_enabled:
                    self._history.append(HistoryObject(message=question, is_sent=True))
                    self._history.append(
                        HistoryObject(message=response.message, is_sent=False)
                    )
                return response
            raise AchcatException((await response.json())['detail'])

    async def close(self):
        await self._session.close()
        self._session = None

    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
