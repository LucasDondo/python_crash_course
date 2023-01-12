reason = ''
while reason != 'exit'.capitalize():

    reason = input('A reason why you like programming: ').capitalize()

    with open('reasons_to_program.txt', 'a') as rtp:
        rtp.write(f'- {reason}\n')
