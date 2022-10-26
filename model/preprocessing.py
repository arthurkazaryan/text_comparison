from googletrans import Translator
from settings import MAKE_TRANSLATION
import string

translator = Translator(service_urls=['translate.googleapis.com'])


def preprocess_data(company_name: str, make_translation: bool = MAKE_TRANSLATION):

    company_name = company_name.translate(str.maketrans('', '', string.punctuation))
    if make_translation:
        company_name = translator.translate(company_name, dest='en').text

    common_words = ['ltd', 'co', 'inc', 'international', 'industries', 'air', 'lines', 'trading',
                    'logistics', 'products', 'industrial', 'corp', 'corporation', 'trade', 'group',
                    'industry', 'industria', 'comercio', 'global']

    company_name_list = [name.lower() for name in company_name.split()]
    company_name_rdy_list = []

    for word in company_name_list:
        if word not in common_words:
            company_name_rdy_list.append(word)

    return ' '.join(company_name_rdy_list)
