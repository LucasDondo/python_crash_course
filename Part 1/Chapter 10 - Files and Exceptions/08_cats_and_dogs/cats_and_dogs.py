filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            print(f'{f.read()}\n')
    except FileNotFoundError:
        print(f'{filename} not found.\n')
