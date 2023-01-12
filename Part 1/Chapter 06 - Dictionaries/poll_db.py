# This script could be a good one. I could create users, give them IDs, etc.
# And also use usernames taken from a prefabricated dictionary (like those for
# Wi-Fi passwords).

import random

languages = ['python', 'css', 'html', 'php', 'c++', 'c', 'javascript']
persons = ['lucas', 'hilario', 'juan ignacio', 'eric']
poll_results = {}

# for number in range(10):
i = 1
while i < 11:
    print
    poll_results[random.choice(persons, 3)] = random.choice(languages, 3)
    # .choice is a method.
    # (persons, X) are arguments.
    i = i+1

for poll_result in poll_results:
    print(
        f'{poll_result.title()} voted for {poll_results[poll_result].title()}.')
    # Where the .title() goes is extremely important: to search the key with the
    # mayus or the shown value.
