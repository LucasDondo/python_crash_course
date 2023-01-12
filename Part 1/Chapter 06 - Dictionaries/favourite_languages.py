favourite_languages = {
    'lucas': 'python',
    'juani': 'css',
    'hilario': 'c++',
}

# For loop used in dictionaries in which keys and values mean the same
for name, favourite_language in favourite_languages.items():
    if favourite_language == 'css':
        print(
            f"{name.title()}'s favourite programming language is {favourite_language.upper()}.")
    else:
        print(
            f"{name.title()}'s favourite programming language is {favourite_language.title()}.")

# How the get() method works
print('\nExamples on the get() method:')
print(favourite_languages.get('Caro'))
print(favourite_languages.get('Caro', 'Caro has no favourite programming language.'))
print(favourite_languages['Caro'])
