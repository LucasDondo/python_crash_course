''' A class that can be used to represent a restaurant. '''


class Restaurant:
    ''' A simple attempt to model a restaurant. '''

    def __init__(self, name, cuisine_type):
        ''' Initialize name and cuisine type attributes. '''

        self.name = name.capitalize()
        self.cuisine_type = cuisine_type
        self.num_served = 0

    def describe_restaurant(self):
        ''' Prints name and cuisine_type. '''

        print(
            f'Welcome to {self.name}, '
            f'where {self.cuisine_type} is the cuisine type!')

    def open_restaurant(self):
        ''' Indicates that the restaurant is open. '''

        print(f'{self.name} is open, come in!')

    def set_number_served(self, new_num_served):
        ''' Helps the user in setting the new num. of customers. '''

        if new_num_served > self.num_served:
            self.num_served = new_num_served
        elif new_num_served == self.num_served:
            print('No changes made.'
                  'New number of customer is the same as the one before.')
        else:
            print(
                'The new number of customers must be more than the one before.')

    def increment_num_served(self, increment_num_served):
        ''' Increment the number of clients served. '''

        if increment_num_served > 0:
            self.num_served += increment_num_served
        else:
            print('The increment number must be higher than 0.')
