from starlette.status import HTTP_400_BAD_REQUEST

from domain.exceptions.base import BaseHTTPException


class TaskNotFoundError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Task not found"


class TaskCreateError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while creating task"


class TaskUpdateError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while updating task"


class TaskRetrieveError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while retrieving task"


class TaskDeleteError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Error while deleting task"


class TaskIntegrityError(BaseHTTPException):
    status_code = HTTP_400_BAD_REQUEST
    message = "Task integrity error"
