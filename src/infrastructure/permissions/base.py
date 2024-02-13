from starlette.requests import Request

from domain.exceptions.user import UserPermissionDenied
from infrastructure.permissions.interfaces import IPermission


class BasePermission(IPermission):
    """Base permission"""

    async def __call__(self, request: Request):
        user = request.state.user

        user_role = user.get("role")
        if not user_role:
            raise UserPermissionDenied

        result = await self.has_permission(user_role)
        if not result:
            raise UserPermissionDenied
        return self
