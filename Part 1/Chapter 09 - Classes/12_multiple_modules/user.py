class User:
    ''' A simple attempt to model users. '''

    def __init__(self, first_name, last_name, username):
        ''' Initialize first and last name. '''

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        ''' It just describes him. '''

        print(f"{self.first_name} {self.last_name}'s "
              f"username is @{self.username}.")

    def greet_user(self):
        ''' Prints a personal message. '''

        print(f'Hello, @{self.username}! Welcome home!')

    def increment_login(self):
        ''' It just updates login_attempts each try. '''

        self.login_attempts += 1

    def reset_login_attempts(self):
        ''' Now, login_attempts is back to 0. '''

        self.login_attempts = 0
