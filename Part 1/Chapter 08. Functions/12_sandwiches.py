def create_sandwich(*items):
    ''' Create a sandwich with the given items. '''

    print('\n--- Sandwich order items ---')
    for item in items:
        print(f'- {item}')


create_sandwich('jam', 'cheese', 'tomato')
create_sandwich('german bread', 'salami')
create_sandwich('lettuce')
