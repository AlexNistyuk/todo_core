from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from infrastructure.managers.database import DatabaseManager
from infrastructure.managers.kafka import KafkaManager
from infrastructure.middlewares.user import UserAuthMiddleware
from presentation.routers import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await DatabaseManager.connect()
    await KafkaManager.connect()

    yield

    await DatabaseManager.close()
    await KafkaManager.close()


middlewares = (UserAuthMiddleware,)

app = FastAPI(lifespan=lifespan)
app.include_router(api_router)
app.add_middleware(UserAuthMiddleware)


# TODO delete in production

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
