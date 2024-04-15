"""
Starting point of the NER service
"""
from app import createapp
from app.config import get_settings

settings = get_settings()
fastapi_app = createapp.get_app(settings)