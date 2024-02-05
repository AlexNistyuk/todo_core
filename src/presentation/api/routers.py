from fastapi import APIRouter

from presentation.api.v1.sheets import router as sheet_router
from presentation.api.v1.tasks import router as task_router

router = APIRouter(prefix="/v1", tags=["V1"])
router.include_router(task_router, prefix="/tasks", tags=["Tasks"])
router.include_router(sheet_router, prefix="/sheets", tags=["Sheets"])
