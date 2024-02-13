import aiohttp
from starlette.status import HTTP_200_OK

from infrastructure.config import get_settings


class UserInfo:
    url = get_settings().user_info_url

    @classmethod
    async def get_user_info(cls, headers) -> dict | None:
        async with aiohttp.ClientSession() as session:
            response = await session.get(cls.url, headers=headers)
            if response.status == HTTP_200_OK:
                return await response.json()
            return None
