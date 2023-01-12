user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

list = ['hello', 'friend', ('italian', 'spanish')]

# Without the items() method, this gets a traceback.
# I suppose that it is that method what gives me the opportunity to create
# multiple variables in a single for loop.
for key, value in user_0.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}')

# How the items() method works
print('\nPrinting the dictionary with the items() method:')
print(user_0.items())

print('\nPrint a list as-is (with a tuple inside one item):')
print(list)  # This looks the same way as a dic.items().
# THAT IS WHAT .ITEMS() DOES! (It returns a dic as a list)

print('\nPrint without it:')
print(user_0)
