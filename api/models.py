from pydantic import BaseModel


class PostDetectionResult(BaseModel):
    status: str
    distance: float
    nearest: str


class GetCompanyNames(BaseModel):
    company_names: list
