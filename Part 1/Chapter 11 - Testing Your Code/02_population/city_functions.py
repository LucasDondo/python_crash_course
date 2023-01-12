def formatted_city(city, country, population=''):
    ''' It just formats the city name. '''

    if population:
        formatted = f'{city}, {country}.\nPopulation: {population}.'.title()
    else:
        formatted = f'{city}, {country}.'.title()
    return formatted
