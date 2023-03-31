sandwich_orders = ['cuban sandwich',
                   'reuben sandwich',
                   'monte cristo sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'I made your {current_sandwich.title()}.')
    finished_sandwiches.append(current_sandwich)

print('\n--- Finished sandwiches ---')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
