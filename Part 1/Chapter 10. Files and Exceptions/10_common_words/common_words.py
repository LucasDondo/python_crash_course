# Comment 1: Once I read the file, the "cursor" ends up at the end of the text,
# so if I want to re-read it, I need to first go back to the beginning.
# https://stackoverflow.com/a/3906148

filenames = ['Christian Foundation, Or, Scientific and Religious Journal.txt',
             'Opportunities in Engineeering.txt']

for filename in filenames:

    try:
        with open(filename) as f:
            print(f'\nIn {filename[:-4]}...')

            print('The number of times "the" appears:')
            print(f.read().lower().count('the'))

            f.seek(0)  # Comment 1
            print('The number of times "the " appears:')
            print(f.read().lower().count('the '))

    except FileNotFoundError:
        print(f'\n{filename[:-4]} has not been found.')
