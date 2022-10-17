from fastapi import APIRouter
from api.models import PostDetectionResult, GetCompanyNames
from fastapi.responses import JSONResponse
from model.fuzzywuzzy import search_nearest
from database.commands import get_companies, add_company

detection_v1 = APIRouter()


@detection_v1.post('/push', tags=['detection'])
async def post_detection(name: str):

    distance, nearest = search_nearest(input_name=name)

    if distance < 0.7:
        add_company(
            company_name=name
        )

    return JSONResponse(
        content=PostDetectionResult(
            status='FOUND' if distance > 0.7 else 'ADDED',
            distance=distance,
            nearest=nearest
        ).dict()
    )


@detection_v1.get('/company_names', tags=['detection'])
async def get_company_names():

    return JSONResponse(
        content=GetCompanyNames(
            company_names=get_companies()
        ).dict()
    )
