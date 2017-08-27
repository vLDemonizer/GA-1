from GA.settings import LOCATIONS, ENTERPRISE


def generate_full_code(enterprise, country, city, dept, code):
    return enterprise + country + '-' + city + '-' + dept + '-' + code + 'S001-0000'
