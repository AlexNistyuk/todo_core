from domain.utils.roles import UserRole
from infrastructure.config import get_settings
from infrastructure.permissions.base import BasePermission

settings = get_settings()


class IsAdmin(BasePermission):
    async def has_permission(self, user_role: str) -> bool:
        return user_role == UserRole.admin.value
