my_foods = ['pizza', 'falafel', 'carrot cake']

# This doesn't work as a copy. This is more of another way to access the
# original list rather than copying it. (Better descibed in the book, on page
# 64)  This does not work automatically with variables, as shown in
# copy_attributes.py.

# friend_food = my_foods

# This one does separate the two lists.
friend_food = my_foods[:]

my_foods.append('cannoli')
friend_food.append('ice cream')

print('My favourites foods are:')
for food in my_foods:
    print(food.title())

print("\nMy friend's favourite foods are:")
for food in friend_food:
    print(food.title())
