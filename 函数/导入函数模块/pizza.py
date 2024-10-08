def make_pizza(size,*tippings):
    print("\nMakeing a " + str(size) + "-inch pizza with following toppings:")
    for tipping in tippings:
        print("-",tipping.upper())