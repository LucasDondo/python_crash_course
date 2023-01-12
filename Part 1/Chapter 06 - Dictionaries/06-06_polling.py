languages = ['c', 'php']

favourite_languages = {
    'lucas': 'python',
    'juani': 'css',
    'hilario': 'c++',
    'steve': languages,  # Or ['c', 'php] directly.
}

who_to_poll = ['lucas', 'caro', 'juani', 'bosco', 'hilario', 'juan cruz']

for person in who_to_poll:
    if person in favourite_languages:
        print(f'{person.title()}, thank you for responding the poll!')
    elif person not in favourite_languages:
        print(f'{person.title()}, you should answer the poll!')

for number in range(30):
    print(number)

# How (I got) to display dictionary items that are lists in a nice way.
for favourite_language in favourite_languages.values():
    type = isinstance(favourite_language, list)
    if type == True:
        for favourite_language_list in favourite_language:
            print(favourite_language_list.title())
    elif type == False:
        print(favourite_language.title())
