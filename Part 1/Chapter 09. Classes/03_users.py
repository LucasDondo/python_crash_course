class User:
    ''' A simple attempt to model users. '''

    def __init__(self, first_name, last_name, username):
        ''' Initialize first and last name. '''

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username

    def describe_user(self):
        ''' It just describes him. '''

        print(f"{self.first_name} {self.last_name}'s "
              f"username is @{self.username}.")

    def greet_user(self):
        ''' Prints a personal message. '''

        print(f'Hello, @{self.username}! Welcome home!')


a = User('facundo', 'peña', 'Facxmon')
a.describe_user()
a.greet_user()
print('')

b = User('lucas', 'dondo', 'LucasDondo')
b.describe_user()
b.greet_user()
print('')

c = User('teresa', 'de jesús avila', 'fideosconmantecayrivotril')
c.describe_user()
c.greet_user()
print('')
