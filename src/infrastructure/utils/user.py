import aiohttp

from infrastructure.config import get_settings


class UserInfo:
    url = get_settings().user_info_url

    @classmethod
    async def get_user_info(cls, headers) -> dict:
        async with aiohttp.ClientSession() as session:
            response = await session.get(cls.url, headers=headers)

            return await response.json()
