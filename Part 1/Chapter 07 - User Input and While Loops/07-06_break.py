message = '\nEnter a pizza topping (or "quit" to exit the program): '
topping = input(message)

while True:
    if topping == 'quit':
        break
    print("I'll add ", topping, "to your pizza.")
    topping = input(message)
