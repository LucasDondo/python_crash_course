favorite_places = {
    'lucas': ['la callecita', 'el rinconcito de jesusito', 'bariloche'],
    'delfi': ['centro gimnástico norte', 'marín'],
    'luz': ['mar del sur'],
}

for name, favorite_places in favorite_places.items():
    if len(favorite_places) == 1:
        print(f"\n{name.title()}'s favorite place is:")
    elif len(favorite_places) > 1:
        print(f"\n{name.title()}'s favorite places are:")
    for favorite_place in favorite_places:
        print(f"\t{favorite_place.title()}")
