number = 1
ordinal_numbers = []

while number <= 9:
    ordinal_numbers.append(number)
    number = number + 1

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(f'{ordinal_number}st')
    elif ordinal_number == 2:
        print(f'{ordinal_number}nd')
    elif ordinal_number == 3:
        print(f'{ordinal_number}rd')
    else:
        print(f'{ordinal_number}th')
