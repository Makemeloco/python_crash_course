from city_functions import get_formatted_city

print("Enter 'q' at any time to quit.")
while True:
    city = input('\nPlease give me a city name: ')
    if city == 'q':
        break
    country = input("Please give me a country name: ")
    if country == 'q':
        break
    population = input("Please give me a population: ")
    if population == 'q':
        break

    formatted_city_name = get_formatted_city(city, country, population)
    print("\tFormatted name: " + formatted_city_name)
