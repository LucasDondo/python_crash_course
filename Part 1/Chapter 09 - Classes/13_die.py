from random import randint


class Die:
    ''' A simple attempt to represent a die. '''

    def __init__(self, sides=6):
        ''' Initialize die attributes. '''
        self.sides = sides

    def roll(self):
        ''' It just simulates the die rolls. '''

        print(f'The die rolled, and the number is... {randint(1, self.sides)}')


def roll_10(die):
    ''' Simulates the die rolls 10 times. '''

    print(f'\nWith a {die.sides}-sided die:')
    i = 1
    while i <= 10:
        die.roll()
        i += 1


die_6 = Die()
roll_10(die_6)

# print('\nWith a 10-sided die:')
die_10 = Die(10)
roll_10(die_10)

# print('\nWith a 20-sided die:')
die_20 = Die(20)
roll_10(die_20)
