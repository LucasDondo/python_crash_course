# I was able to do it nicer just when I saw the resolution...
# My 100% original attempt (06_addition.py) was horrible.

print("Give me two numbers, and I'll sum them up!")
print('Press "q" to quit.')

while True:

    try:
        x = input('\nFirst number: ')
        if x == 'q':
            break
        x = int(x)

        y = input('Second number: ')
        if y == 'q':
            break
        y = int(y)

        print(f'{x} + {y} = {x + y}')

    except ValueError:
        print('Please enter a valid number.')

print("\nSee ya, brother!")
