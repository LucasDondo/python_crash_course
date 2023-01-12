import json


def get_stored_username():
    ''' Get stored username if available. '''

    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    ''' Prompt for a new username. '''

    username = input("What is your name? ").capitalize()
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        return username


def greet_user():
    ''' Greet the user by name. '''

    username = get_stored_username()

    if username:
        correct_usr = input(
            f'Is {username} the correct username? (Yes/No) ').capitalize()
        if correct_usr == 'Yes':
            print(f"Welcome back, {username}!")
        elif correct_usr == 'No':
            print("\nLet's create a new username!")
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()


greet_user()
