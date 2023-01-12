from random import choice

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ['A', 'B', 'C', 'D', 'E']
characters = nums + letters


my_ticket = [choice(characters), choice(characters),
             choice(characters), choice(characters)]
winner_ticket = [choice(characters), choice(characters),
                 choice(characters), choice(characters)]
i = 0

while my_ticket != winner_ticket:
    winner_ticket = [choice(characters), choice(characters),
                     choice(characters), choice(characters)]
    print(f'The winner is... {winner_ticket}')
    i += 1

print(f'\nYour ticket: {my_ticket}')
print(f'Winner ticket: {winner_ticket}')
print(f'{i} tickets had been taken before yours appeared.')
