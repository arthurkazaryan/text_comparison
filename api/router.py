from fastapi import APIRouter
from api.models import PostDetectionResult, GetCompanyNames
from fastapi.responses import JSONResponse
from model.preprocessing import preprocess_data
from model.predict import encode_company_name, search_nearest
from database.commands import get_companies, add_company

detection_v1 = APIRouter()


@detection_v1.post('/push', tags=['detection'])
async def post_detection(name: str):

    name = preprocess_data(company_name=name)
    encoded_name = encode_company_name(company_name=name)
    distance, nearest = search_nearest(encoded_company_vector=encoded_name)

    if distance < 0.7:
        add_company(
            company_name=name,
            company_encoded_array=encoded_name
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
            company_names=[c_name for c_name, _ in get_companies()]
        ).dict()
    )
