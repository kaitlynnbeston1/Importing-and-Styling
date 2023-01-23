def print_models(unprinted_designs, completed_models):
    """ 
    Simulates printing each design, until none are left.
    move each design to completed_moddels after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
    
def show_completed_models(completed_models):
    """Shows all models that have been printed. """
    print("The following models have been printed:")
    for model in completed_models:
        print(model)
