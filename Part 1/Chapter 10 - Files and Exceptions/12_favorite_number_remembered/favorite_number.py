import json

filename = 'favorite_number.json'


def load_fav_num():
    ''' It simply loads the favorite number. '''

    with open(filename)as f:
        fav_num = json.load(f)
    print(f"I know your favorite number! It's {fav_num}.")


def ask_fav_num():
    ''' It simply asks the user their favorite number. '''

    while True:
        try:
            fav_num = int(input('Your favorite number: '))
            return fav_num
            break
        except ValueError:
            print('It must be a number!')


def save_fav_num(fav_num):
    ''' It simply saves the favorite number. '''

    with open(filename, 'w') as f:
        json.dump(str(fav_num), f)


def main():
    ''' Combination of everything, to create the perfect program. '''
    try:
        load_fav_num()
    except FileNotFoundError:
        fav_num = ask_fav_num()
        save_fav_num(fav_num)
        load_fav_num


main()
