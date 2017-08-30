from GA import settings

def generate_full_code(user, product, number):
    serie = 0
    if number >= 100000000:
        serie = number / 100000000
        number = number % 100000000
    enterprise = settings.ENTERPRISE_DIC[user.enterprise]
    country = settings.COUNTRY_DIC[user.country]
    city = settings.CITY_DIC[user.city]
    dept = settings.DEPARTMENTS_DIC[product.department]
    code = product.code

    return (
        enterprise +
        country + '-' +
        city + '-' +
        dept + '-' +
        code + '-' +
        'S' + format(serie, '05d') + '-' +
        format(number, '08d')
    )
