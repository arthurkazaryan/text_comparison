from googletrans import Translator
from settings import MAKE_TRANSLATION
import string

translator = Translator(service_urls=['translate.googleapis.com'])


def preprocess_data(company_name: str, make_translation: bool = MAKE_TRANSLATION):

    company_name = company_name.translate(str.maketrans('', '', string.punctuation))
    if make_translation:
        company_name = translator.translate(company_name, dest='en').text

    return company_name.lower()
