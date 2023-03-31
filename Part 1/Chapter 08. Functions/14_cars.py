# In this v2., I made the code easier to understand by using the solutions web
# site.

def make_car(manufacturer, model_name, **specs):
    ''' Make a dic. representing a car. '''

    new_car = {
        'manufacturer': manufacturer,
        'model_name': model_name,
    }
    # Using this order of code, the logged info. is in the correct order in the
    # outputted dic.
    for spec, val in specs.items():
        new_car[spec] = val

    return new_car


car = make_car(
    'honda',
    'pilot',
    size='big',
    location='argentina',
)

print(car)
