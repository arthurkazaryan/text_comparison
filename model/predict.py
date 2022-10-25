from database.commands import add_company, get_companies
from database.main import convert_array
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from settings import MODEL_NAMES, MODEL_SELECTION
import numpy as np


model = SentenceTransformer(MODEL_NAMES[MODEL_SELECTION])


def encode_company_name(company_name: str):

    all_companies = get_companies()

    for c_name, c_array in all_companies:
        if c_name == company_name:
            encoded_company_vector = convert_array(c_array)
            return encoded_company_vector

    encoded_company_vector = model.encode(company_name)

    return encoded_company_vector


def search_nearest(encoded_company_vector: np.ndarray):

    distance = 0
    nearest = ''

    all_companies = get_companies()

    for c_name, c_array in all_companies:
        cos_distance = cosine_similarity(encoded_company_vector.reshape(1, -1), convert_array(c_array).reshape(1, -1))[0][0]
        if cos_distance > distance:
            distance = cos_distance
            nearest = c_name

    return distance, nearest
