pet0 = {
    'animal': 'dog',
    'name': 'loli',
    'owner': 'lucas',
}

pet1 = {
    'animal': 'dog',
    'name': 'arthur',
    'owner': 'caro',
}

pet2 = {
    'animal': 'cat',
    'name': 'inti',
    'owner': 'norma',
}

pets = [pet0, pet1, pet2]

for pet in pets:
    print(f"\n{pet['owner'].title()} owns a {pet['animal']} called "
          f"{pet['name'].title()}.")
