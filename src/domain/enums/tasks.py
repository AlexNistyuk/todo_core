import enum


class TaskActionType(enum.Enum):
    create = "create"
    retrieve = "retrieve"
    done = "done"
