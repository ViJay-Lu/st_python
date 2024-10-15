#01_定义函数
def print_username():
    print('vijay')

print_username()
print('--------------------------------')

#02_传参
def greet_user(username):
    print('hello,' + username)

greet_user('yoyo')
print('--------------------------------')

#03_位置实参
def describe_pet(animal_type,pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name)

describe_pet("cat","duoduo")
describe_pet(animal_type="cat",pet_name="duoduo")
describe_pet(pet_name="duoduo",animal_type="cat")
describe_pet("dog","xiangxiang")

print('--------------------------------')
#04_函数默认值
def describe_pet(animal_type,pet_name="duoduo"):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name)

describe_pet("cat")
describe_pet("dog","wangcai")