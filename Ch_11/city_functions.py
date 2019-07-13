def get_formatted_city(city, country, population=''):
    """Отображает отформатированное название города и страны."""
    if population:
        city_country = city.title() + ', ' + country.title() + ' — population ' + population + '.'
    else:
        city_country = city.title() + ', ' + country.title() + '.'

    return city_country
