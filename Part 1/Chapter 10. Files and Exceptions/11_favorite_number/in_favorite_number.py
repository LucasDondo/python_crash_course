import json

filename = 'favorite_number.json'
while True:
    try:
        fav_num = int(input('Your favorite number: '))
        break
    except ValueError:
        print('It must be a number!')

with open(filename, 'w') as f:
    json.dump(str(fav_num), f)
