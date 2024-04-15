"""
Includes model related routes. All endpoints exposed in this module.
"""
from fastapi import APIRouter

from app.datamodels.model import NERRequest, NERResponse
from app.services.modelservice import ModelService

model_service: ModelService

async def startup():
    """
    Create model service instance
    :return:
    """
    global model_service
    model_service = ModelService()


async def shutdown():
    """
    Clean up the model service and release the resources
    :return:
    """
    global model_service
    model_service.clear()

router = APIRouter(on_startup=[startup], on_shutdown=[shutdown])

@router.post("/name-entity-recognition", response_model=NERResponse)
async def name_entity_recognition(request: NERRequest):
    global model_service
    ner_ = model_service.get_ner(request.text)
    return NERResponse(ner=ner_)