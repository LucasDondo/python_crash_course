def describe_city(name, country='argentina'):
    ''' Display a message about the city. '''
    print(f'{name.title()} is in {country.title()}.')


describe_city('san isidro',)
describe_city('tigre',)
describe_city('barcelona', 'españa')
