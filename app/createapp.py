"""
Create and configure the fastapi app
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import Settings
from app.routers import model


def get_app(settings: Settings):
    """
    Create fastapi instance. Add router from different module.
    To block/allow the end points add cors middleware
    :return: FastAPI
    """
    # create fastApi app
    app = FastAPI()

    # include routers
    app.include_router(model.router)

    # add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allow_origins,
        allow_credentials=settings.allow_credentials,
        allow_methods=settings.allow_methods,
        allow_headers=settings.allow_headers,
    )

    return app
