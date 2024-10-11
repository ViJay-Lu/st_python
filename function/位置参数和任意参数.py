from dict.字典嵌套 import location


def make_pizza(size,*tippings):
    print("\nMakeing a " + str(size) + "-inch pizza with following toppings:")
    for tipping in tippings:
        print("-",tipping.upper())

make_pizza(12,"pepperoni")
make_pizza(3,"mushrooms","green peppers","extra cheese")

def build_users(first,last,**user_info):
    """创建一个空字典"""
    users = {}
    users["firstname"] = first
    users["lastname"] = last
    for key,value in user_info.items():
        users[key] = value
    return users

user_profile = build_users("lu","vijay",
                           location="princeton",
                           field="physics")
print(user_profile)