favourite_numbers = {
    'caro': 20,
    'lucas': 20,
    'belén': 1000,
    'luz': 5,
    'agus': 125,
}

# This could also be made with the get() method.
for favourite_number in favourite_numbers:
    print(
        f"{favourite_number.title()}'s favourite number is"
        f" {favourite_numbers[favourite_number]}.")
