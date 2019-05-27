def city_country(city, country):
    """Возвращает аккуратно отформатированные значения."""
    full_vars = city + ', ' + country
    return full_vars.title()

geo = city_country('voronezh', 'russia')
print(geo)

geo = city_country('leon', 'france')
print(geo)

geo = city_country('berlin', 'germany')
print(geo)
