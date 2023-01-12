pizzas = ['muzarella', 'ham', 'broccoli']
for pizza in pizzas:
    print(f'One of my favourite pizzas is {pizza} pizza!')
print('Although, pizza is not my favourite food.')

# Exercise 4.11 (page 65)
friend_pizzas = pizzas[:]
pizzas.append('parsley')
friend_pizzas.append('pita')

print('My favourite pizzas are:')
for pizza in pizzas:
    print(pizza)
print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
