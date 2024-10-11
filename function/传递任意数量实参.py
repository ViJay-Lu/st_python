"""在python中，*让python创建一个名为toppings的空元组，并将所有的值都风封装在这个元组中"""
def make_pizza(*toppings):
    """概述要制作的披萨"""
    print('\nMakeing a pizza with following toppings:')
    for topping in toppings:
        print("-",topping.title())
"""
Makeing a pizza with following toppings:
- Pepperoni
"""
make_pizza("pepperoni")

"""
Makeing a pizza with following toppings:
- Mushrooms
- Green peppers
- Extra cheese
"""
make_pizza("mushrooms","green peppers","extra cheese")