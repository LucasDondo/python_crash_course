import printing_functions as pf

models_to_print = pf.ask_models()

pf.show_models_to_print(models_to_print)

printed_models = pf.print_models(models_to_print)

pf.show_printed_models(printed_models)
