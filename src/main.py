from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from application.dependencies import Container
from infrastructure.managers.database import DatabaseManager
from infrastructure.managers.kafka import KafkaManager
from infrastructure.middlewares.auth_middleware.init import init_auth_middleware
from presentation.routers import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await DatabaseManager.connect()
    await KafkaManager.connect()

    container = Container()
    container.wire(
        modules=[
            "presentation.api.v1.sheets",
            "presentation.api.v1.tasks",
            "presentation.api.v1.statuses",
        ]
    )

    yield

    await DatabaseManager.close()
    await KafkaManager.close()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)

# TODO mek a function like init_auth_middleware

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_auth_middleware(app)
