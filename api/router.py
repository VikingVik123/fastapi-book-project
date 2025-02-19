from fastapi import APIRouter
from api.routes import integration_conf
from api.routes import books

api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])
api_router.include_router(integration_conf.router)
