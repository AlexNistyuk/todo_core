from fastapi import APIRouter

from presentation.api.v1.lists import router as list_router
from presentation.api.v1.tasks import router as task_router

router = APIRouter(prefix="/v1", tags=["V1"])
router.include_router(task_router, prefix="/tasks", tags=["Tasks"])
router.include_router(list_router, prefix="/lists", tags=["Lists"])
