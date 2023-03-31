print("Give me two numbers and I'll sum them up!")
print('Press "q" to quit.')


def ask_nums():
    try:
        nums = ['', '']

        num_a = input('\nFirst number: ')
        if num_a == 'q':
            print('\nIt was nice to meet you!')
            exit()
        else:
            nums[0] = int(num_a)

        num_b = input('Second number: ')
        if num_b == 'q':
            print('\nIt was nice to meet you!')
            exit()
        else:
            nums[1] = int(num_b)

        return nums
    except ValueError:
        print('You must enter a number.')
        nums = ask_nums()
        return nums


nums = ask_nums()
print(nums)
print(f'\n{nums[0]} + {nums[1]} = {nums[0] + nums[1]}')
