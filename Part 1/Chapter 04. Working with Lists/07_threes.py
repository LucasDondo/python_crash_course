threes=list(range(3, 31, 3))

multiplier=1
for three in threes:
    print(f"3x{multiplier}={three}")
    multiplier =multiplier+1

# Exercise 4.10 (page 103)
print("The first three items in the list are:")
for three in threes[:3]:
    print(three)
print('Three items from the middle of the list are:')
for three in threes[3:6]:
    print(three)
print('The last three items in the list are:')
for three in threes[-3:]:
    print(three)