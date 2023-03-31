squares = [value**2 for value in range(1, 11)]
print(squares)

list_comprehension = [str(value)+"1" for value in range(1, 11)]
print(list_comprehension)
list_comprehension.append(1)
print(list_comprehension)
