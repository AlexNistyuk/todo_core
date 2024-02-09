import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI

from application.providers.providers import Container
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


def init_user_middleware(app: FastAPI, ignore_paths: tuple):
    app.add_middleware(UserAuthMiddleware, ignore_paths=ignore_paths)


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)

init_user_middleware(app, ignore_paths=("/docs", "/openapi.json"))

container = Container()
container.wire(modules=[sys.modules[__name__]])
