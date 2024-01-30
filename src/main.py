from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from infrastructure.config import get_settings
from infrastructure.managers.database import DatabaseManager
from presentation.api.routers import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_manager = await DatabaseManager.connect()

    yield

    await db_manager.close()


app = FastAPI()
app.include_router(api_router)


# TODO delete in production

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=get_settings().web_port)
