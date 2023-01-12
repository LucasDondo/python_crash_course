rivers = {
    'mississippi': 'united states of america',
    'ganges': 'india',
    'thames': 'england',
}

for river, country in rivers.items():
    print(f'The {river.title()} river can be found in {country.title()}.')

print()
for river in rivers:
    print(river.title())

print()
for country in rivers.values():
    print(country.title())

print(rivers.items())
