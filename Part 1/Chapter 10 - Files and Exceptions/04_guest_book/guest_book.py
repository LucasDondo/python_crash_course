print('Welcome to Hotel Emperador!')
guest = ''

while guest != 'exit'.title():

    guest = input('\nYour name: ').title().strip()
    with open('guest_book.txt') as gb:

        if guest == 'exit'.title():
            print('\nWell, well, too much job for today, good night everyone!')

        elif guest not in gb.read():
            print(f'Hello, {guest}, nice to meet you. Come on in!')
            with open('guest_book.txt', 'a') as gb_a:
                gb_a.write(f'\n- {guest}')
            print('\nNext one on the line please!')

        else:
            print(f'{guest}, nice to see you again!')
            print('\nNext one on the line please!')
