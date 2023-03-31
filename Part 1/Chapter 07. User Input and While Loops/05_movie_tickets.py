age = int

while True:
    age = int(input('How old are you? '))

    if age <= 3 and age >= 0:
        print('Your ticket is free!')
    elif age > 3 and age <= 12:
        print('Your ticket is $10.')
    elif age >= 12:
        print('Your ticket is $15.')
