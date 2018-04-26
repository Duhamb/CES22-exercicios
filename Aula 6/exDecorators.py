# Decorator example using arguments list and arguments dictionary

def decorator_shopping_list(original_function):
    def wrapper_function(*args, **kwargs):
        print("    SHOPPING  LIST    ")
        print("Item          Quantity")
        print("----------------------")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_shopping_list
def shopping_list(itens, quantity):
    for item in itens:
        print("{:<10}{:>12}".format(item, quantity[item]))

itens = ['bean', 'bread', 'butter', 'eggs', 'milk', 'rice', 'soap']
quantity = {'bean': 1, 'bread': 8, 'butter': 1, 'eggs': 12, 'milk': 1, 'rice': 1, 'soap': 3}
shopping_list(itens, quantity)