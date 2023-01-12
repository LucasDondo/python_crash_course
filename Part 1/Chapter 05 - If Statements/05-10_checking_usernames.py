current_users = ['caro', 'lucas', 'belén', 'admin', 'huevo', 'mago']
new_users = ['carito', 'luquitas', 'delfi', 'admin', 'Huevo', 'santi']
current_users_lower = []

for current_user in current_users:
    current_users_lower.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'The username \x1B[3m{new_user}\x1B[0m has already been used. \
You need to enter another one.')
    else:
        print(f'The username \x1B[3m{new_user}\x1B[0m is available!')
