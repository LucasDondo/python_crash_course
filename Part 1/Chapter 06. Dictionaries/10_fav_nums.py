fav_nums = {
    'caro': [20, 22, 21],
    'lucas': [20, 22, 27],
    'belén': [1000, 80],
    'luz': [5, 1, 3],
    'agus': [125],
}

# This could also be made with the get() method.
for person, fav_nums in fav_nums.items():
    if len(fav_nums) == 1:
        print(f"\n{person.title()}'s favourite number is:")
    elif len(fav_nums) > 1:
        print(f"\n{person.title()}'s favourite numbers are:")
    for fav_num in fav_nums:
        print(f"\t· {fav_num}")
