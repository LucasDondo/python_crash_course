responses = {}
polling_active = True

while polling_active:
    name = input('Hello! How is your name? ')
    answer = input(
        'If you could visit one place in the world, where would you go? ')
    responses[name] = answer
    quit = input(
        'Is there someone else who wants to answer the poll? (yes/no) ')
    if quit == 'no':
        polling_active = False

print('\n--- Poll results ---')
for name, answer in responses.items():
    print(f'{name} wants to go to {answer}.')
