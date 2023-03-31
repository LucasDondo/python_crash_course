cities = {

    'san isidro': {
        'country': 'argentina',
        'population': 45_190,
        'fact': "it ranks as the province's most affluent neighborhood.",
    },

    'washington': {
        'country': 'united states of america',
        'population': 692_683,
        'fact': "it's defined by imposing neoclassical monuments and buildings",
    },

    'paris': {
        'country': 'france',
        'population': 2_161_000,
        'fact': "it's a global center for art, fashion, gastronomy and culture.",
    },
}

for city, info in cities.items():
    print(city.title())
    for data in info.values():
        if type(data) == int:
            print(f'\t{"{:,}".format(data)}')
        elif type(data) == str:
            print(f'\t{data.capitalize()}')
