message = '\nEnter a pizza topping (or "quit" to exit the program): '
topping = input(message)

while topping != 'quit':
    print("I'll add ", topping, "to your pizza.")
    topping = input(message)
