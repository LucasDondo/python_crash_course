def create_car(manufacturer, model_name, **car):  # "**car" creates the dic. and
    ''' Make a dic. representing a car. '''      # assigns the kwargs. to it.
    car['manufacturer'] = manufacturer           # Then the other args are
    car['model_name'] = model_name               # inserted into it.
    return car


car = create_car('honda', 'pilot', size='big', location='argentina')
print(car)
