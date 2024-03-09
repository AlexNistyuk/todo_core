from starlette.status import HTTP_400_BAD_REQUEST

from domain.exceptions.base import BaseHTTPException


class StatusNotFoundError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Status not found"


class StatusCreateError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while creating status"


class StatusUpdateError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while updating status"


class StatusRetrieveError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while retrieving status"


class StatusDeleteError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while deleting status"


class StatusIntegrityError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Status integrity error"
