# user_input = None
# user_input1 = None

# while user_input != 'Q' or user_input1 != 'Q':
#     user_input = input('Tell me, 0: ')
#     print(user_input)
#     user_input1 = input('Tell me, 1: ')
#     print(user_input1)

# for i in range(1, 101):

#     id = exec('id_' + str(i))
#     print(id)

album = '12 historias'

for i in range(1, 101):
    id = 'id_' + str(i)
    exec(id + "= 'album'")
    print(id)
