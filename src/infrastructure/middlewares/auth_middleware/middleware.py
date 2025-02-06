import typing

from aiohttp import ClientConnectorError
from starlette.middleware.base import (
    BaseHTTPMiddleware,
    DispatchFunction,
    RequestResponseEndpoint,
)
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

from infrastructure.utils.user import UserInfo


class AuthMiddleware(BaseHTTPMiddleware):
    """Set current user to request"""

    def __init__(
        self,
        app: ASGIApp,
        ignore_paths: tuple,
        dispatch: typing.Optional[DispatchFunction] = None,
    ):
        super().__init__(app, dispatch)
        self.ignore_paths = ignore_paths

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        if request.url.path not in self.ignore_paths:
            try:
                user = await UserInfo.get_user_info(request.headers)
            except ClientConnectorError:
                return Response(status_code=503)

            if not user:
                return Response(status_code=401)

            request.state.user = user

        return await call_next(request)
