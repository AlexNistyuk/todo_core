from fastapi import FastAPI

from infrastructure.middlewares.auth_middleware.middleware import AuthMiddleware


def init_auth_middleware(app: FastAPI, ignore_paths=("/docs", "/openapi.json")):
    app.add_middleware(AuthMiddleware, ignore_paths=ignore_paths)
