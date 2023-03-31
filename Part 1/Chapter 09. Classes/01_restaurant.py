class Restaurant:
    ''' A simple attempt to model a restaurant. '''

    def __init__(self, name, cuisine_type):
        ''' Initialize name and cuisine type attributes. '''

        self.name = name.capitalize()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        ''' Prints name and cuisine_type. '''

        print(
            f'Welcome to {self.name}, '
            f'where {self.cuisine_type} is the cuisine type!')

    def open_restaurant(self):
        ''' Indicates that the restaurant is open. '''

        print(f'{self.name} is open, come in!')


a_restaurant = Restaurant("alfredo's", 'argentinian')
a_restaurant.describe_restaurant()
a_restaurant.open_restaurant()
print('')

b_restaurant = Restaurant("carola's", 'traditional')
b_restaurant.describe_restaurant()

c_restaurant = Restaurant("lucas'", 'italian')
c_restaurant.describe_restaurant()
