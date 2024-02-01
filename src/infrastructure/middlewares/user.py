from aiohttp import ClientConnectorError
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from infrastructure.utils.user import UserInfo


class UserAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        if request.url.path not in {"/docs", "/openapi.json"}:
            try:
                user = await UserInfo.get_user_info(request.headers)
            except ClientConnectorError:
                return Response(status_code=503)

            if not user:
                return Response(status_code=401)

            request.state.user = user

        return await call_next(request)
