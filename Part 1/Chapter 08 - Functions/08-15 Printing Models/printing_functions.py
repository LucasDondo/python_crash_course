''' Functions related to 3D printing. '''


def ask_models():
    ''' Ask the user for models to print. '''
    models_to_print = []
    active = True
    print('\nTo stop adding models, press Q and ENTER.\n')

    while active:
        model = input('Insert the model you want to print: ')
        model = model.title()
        if model == 'Q':
            active = False
        else:
            models_to_print.append(model)

    return models_to_print


def show_models_to_print(models_to_print):
    ''' Show the user the models that will be printed. '''
    print('\nThe model to be printed out are:')
    for model in models_to_print:
        print(f'- {model}')


def print_models(models_to_print):
    ''' Simulates that models are being printed. '''
    print('\nNow, we are trying to print the models:\n')
    printed_models = []
    while models_to_print:
        printing_model = models_to_print.pop(0)
        print(f'Printing model: {printing_model.title()}...')
        print('Done!\n')
        printed_models.append(printing_model)
    return printed_models


def show_printed_models(printed_models):
    ''' Shows the user the models that have been printed. '''
    print('\n The printed models are:')
    for model in printed_models:
        print(f'- {model.title()}')
