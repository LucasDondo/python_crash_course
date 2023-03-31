age = 0

while age >= 0:
    age = int(input('How old are you? '))

    if age <= 3 and age >= 0:
        print('Your ticket is free!')
    elif age > 3 and age <= 12:
        print('Your ticket is $10.')
    elif age >= 12:
        print('Your ticket is $15.')

print("\nI don't talk with liers!")
