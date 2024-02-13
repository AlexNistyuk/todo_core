import enum


class TaskActionType(enum.Enum):
    create = "create"
    retrieve = "retrieve"
    done = "done"


class TaskStatus(enum.Enum):
    in_progress = "in_progress"
    done = "done"
