from starlette.status import HTTP_400_BAD_REQUEST

from domain.exceptions.base import BaseHTTPException


class ListNotFoundError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "List not found"


class ListCreateError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while creating task list"


class ListUpdateError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while updating task list"


class ListRetrieveError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while retrieving task list"


class ListDeleteError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while deleting task list"


class ListIntegrityError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "List integrity error"
