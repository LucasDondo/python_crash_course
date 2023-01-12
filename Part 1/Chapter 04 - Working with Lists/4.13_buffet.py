foods = ('spaghetti', 'meat', 'sandwich', 'empanada', 'breaded')

print('Original menu:')
for food in foods:
    print(f'- {food.title()}')

# foods[0] = 'pasta'

foods = ('pasta', 'chicken', 'sandwich', 'empanada', 'breaded')
print('\nNew menu:')
for food in foods:
    print(f'- {food.title()}')
