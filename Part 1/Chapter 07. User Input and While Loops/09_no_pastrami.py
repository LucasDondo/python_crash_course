sandwich_orders = ['cuban sandwich',
                   'pastrami',
                   'reuben sandwich',
                   'pastrami',
                   'monte cristo sandwich',
                   'pastrami',
                   ]
finished_sandwiches = []

print('Deli has sadly run out of pastrami.\n')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'I made your {current_sandwich.title()}.')
    finished_sandwiches.append(current_sandwich)

print('\n--- Finished sandwiches ---')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
