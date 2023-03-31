# By reading the entire file:
print('By reading the entire file:')
with open('learning_python.txt') as lp:
    print(lp.read().rstrip())

# By looping over the file object:
print('\nBy looping over the file object:')
with open('learning_python.txt') as lp:
    for line in lp:
        print(line.rstrip())

# By storing the lines in a list and then working with them outside the with
# block:
print('\nBy storing the lines in a list and then working with them outside ' +
      'the with block:')
text = ''
with open('learning_python.txt') as lp:
    for line in lp.readlines():  # lp.readlines() is a list.
        text += line
print(text)
