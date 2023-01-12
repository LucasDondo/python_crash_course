# Tests for equality and inequality with strings
folder_name = "Carolita Y Luquitas"
folder_name_mins = folder_name.lower()

print("Is folder_name != folder_name_mins? I predict True.")
print(folder_name != folder_name_mins)

print("\nIs folder_name != folder_name_mins.title()? I predict False.")
print(folder_name != folder_name_mins.title())

# Tests using the lower() method
name = "Lucas"

print("\nIs name.lower() == 'lucas'? I predict True.")
print(name.lower() == "lucas")

print("\nIs name.lower() == 'Lucas'? I predict False.")
print(name.lower() == "Lucas")

# Numerical tests involving:
#   Equality and inequality
months_friends = 24
months_dating = 3

print("\nIs months_friends != months_dating? I predict True.")
print(months_friends != months_dating)

print("\nIs months_friends == months_dating? I predict False.")
print(months_friends == months_dating)

#   Greater than and less than
print("\nIs months_friends < months_dating? I predict False.")
print(months_friends < months_dating)

print("\nIs months_dating < months_friends? I predict True.")
print(months_dating < months_friends)

#   Greater than or equal to
special_dates = [3, 7, 20, 21, 22, 27]

print("\nIs months_dating >= 3? I predict True.")
print(months_dating >= 3)

print("\nIs months_friends >= 27? I predict False.")
print(months_friends >= special_dates[5])

#   Less than or equal to
print("\nIs months_friends <= months_dating? I predict False.")
print(months_friends <= months_dating)

print("\nIs months_dating <= 3? I predict True.")
print(months_dating <= 3)

# Tests using the and keyword
print("\nIs folder_name == 'carolita y luquitas' and \
folder_name_mins == 'carolita y luquitas'? I predict False.")
print(folder_name == 'carolita y luquitas' and
      folder_name_mins == 'carolita y luquitas')

print("\nIs folder_name == 'Carolita Y Luquitas' and \
folder_name_mins.title() == 'Carolita Y Luquitas'? I predict True.")
print(folder_name == 'Carolita Y Luquitas' and
      folder_name_mins.title() == 'Carolita Y Luquitas')

# Test using the or keyword
are_we_crazy = True

print("\nIs months_dating == 3 or \
folder_name == 'Carolina Díaz Patterson; Lucas Dondo'? I predict True.")
print(months_dating == 3 or
      folder_name == 'Carolina Díaz Patterson; Lucas Dondo')

print("\nIs folder_name == 'los loquitos' or \
are_we_crazy == False? I predict False.")
print(folder_name == 'los loquitos' or are_we_crazy == False)

# Test whether an item is in a list
things_to_do = ['Watch Unplanned', 'Watch Los Peques', 'Go for a run']

print("\nIs 'Go for a run' in things_to_do? I predict True.")
print('Go for a run' in things_to_do)

print("\nIs 'Go somewhere elegant with reservation' in things_to_do? \
I predict False.")
print('Go somewhere elegant with reservation' in things_to_do)

# Test whether an item is not in a list
print("\nIs 'Watch Unplanned' not in things_to_do? I predict False.")
print('Watch Unplanned' not in things_to_do)

print("\nIs 'Watch La La Land' not in things_to_do? I predict True.")
print('La La Land' not in things_to_do)
