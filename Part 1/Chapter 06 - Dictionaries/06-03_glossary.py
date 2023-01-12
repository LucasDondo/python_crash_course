programming_words = {
    'interpreter': 'It is the software in charge of understanding what each \
block of code means and following those instructions.',
    'traceback': 'It is an error log shown when the Python interpreter runs \
into trouble when executing the code.',
    'tuple': 'It is like the constant for variables, but for lists. You use \
() instead of [].',
    'float': 'It is a number with a decimal point. Integers are those without \
a decimal point.',
    'method': 'It is an action that Python can perform on certain data. It \
indicated how that data should behave. cars.sort()',
    'function': 'It is any piece of code we type that gives certain \
instructions. Unlike methods, it is not dependant on some other data. print().',
    'set': "It functions like a list or dictionary, but it ignores duplicated \
items when printing them. The structure is set = {'hello', 'world'}, or \
set(dictionary()).",
    'slice': 'It is a specific group of items in a list.',
    'whitespace': 'It is anything from tabs, spaces and end-of-line symbols.',
    'indentation': 'It is whitespaces that determine how a line is related \
with the rest of the program, it makes code very easy to read with a clear \
visual structure and it also improves organization.',
}

for programming_word in programming_words:
    if programming_word == 'interpreter':
        print('\033[1m' + f'What is an {programming_word}?' + '\033[0m' +
              f'\n{programming_words[programming_word]}\n')
    else:
        print('\033[1m' + f'What is a {programming_word}?' + '\033[0m' +
              f'\n{programming_words[programming_word]}\n')
