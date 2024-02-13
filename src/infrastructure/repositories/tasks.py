from infrastructure.models.tasks import Task
from infrastructure.repositories.base import BaseRepository


class TaskRepository(BaseRepository):
    model = Task
