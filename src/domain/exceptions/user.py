from starlette.status import HTTP_403_FORBIDDEN

from domain.exceptions.base import BaseHTTPException


class UserPermissionDenied(BaseHTTPException):
    status_code = HTTP_403_FORBIDDEN
    message = "Permission denied"
