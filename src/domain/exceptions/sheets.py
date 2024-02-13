from starlette.status import HTTP_400_BAD_REQUEST

from domain.exceptions.base import BaseHTTPException


class SheetNotFoundError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Sheet not found"


class SheetCreateError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while creating task sheet"


class SheetUpdateError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while updating task sheet"


class SheetRetrieveError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while retrieving task sheet"


class SheetDeleteError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while deleting task sheet"


class SheetIntegrityError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Sheet integrity error"
