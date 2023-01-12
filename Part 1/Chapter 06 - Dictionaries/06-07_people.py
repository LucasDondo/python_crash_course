person0 = {
    'first_name': 'caro',
    'last_name': 'díaz patterson',
    'age': 18,
    'city': 'béccar, san isidro',
}

person1 = {
    'first_name': 'lucas',
    'last_name': 'dondo',
    'age': 18,
    'city': 'béccar, san isidro',
}

person2 = {
    'first_name': 'josé juan bosco',
    'last_name': 'arata',
    'age': 18,
    'city': 'béccar, san isidro',
}

people = [person0, person1, person2]

for person in people:
    print(f"\nHello {person['first_name'].title()} "
          f"{person['last_name'].title()}, "
          f"are you {person['age']} years old and live in "
          f"{person['city'].title()}?")
