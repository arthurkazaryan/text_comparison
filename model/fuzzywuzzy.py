from database.commands import add_company, get_companies
from fuzzywuzzy import process


def search_nearest(input_name: str, company_names: list):
    distance = 0
    nearest = ''

    a = process.extract(input_name, company_names, limit=len(company_names))

    for pair in a:
        c_name, dist = pair
        if dist / 100 > distance:
            distance = dist / 100
            nearest = c_name

    return distance, nearest
