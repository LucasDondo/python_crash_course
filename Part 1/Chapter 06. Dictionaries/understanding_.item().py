# More info. is available in user.py.

# The items() method returns a view object. The view object contains the
# key-value pairs of the dictionary, as tuples in a list.
# The view object will reflect any changes done to the dictionary, see example
# below. (https://www.w3schools.com/python/ref_dictionary_items.asp)

dic = {'key0': 'value0', 'key1': 'value1', 'key2': 'value2'}

print('print(dic):')
print(dic)

print('\nprint(dic.items()):')
print(dic.items())

print('\nfor key in dic:')
for key in dic:
    print(key)

print('\nfor key in dic.items():')
for key in dic.items():
    print(key)

print('\nfor key in dic.values():')
for key in dic.values():
    print(key)

print('\nfor key, value in dic.items():')
for key, value in dic.items():
    print(key, value)
