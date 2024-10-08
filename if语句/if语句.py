
'''
hello,my name is vijay
hi,my name is yoyo
hi,my name is lilian
'''
my_family = ['vijay','yoyo','lilian']
if my_family[0] == 'vijay':
    print('hello,my name is',my_family[0])
if my_family[1] == 'yoyo':
    print('hi,my name is',my_family[1])
if my_family[2] == 'lilian':
    print('hi,my name is',my_family[2])

#age < 5,price is $10
age = 11
if age < 5:
    price = 1
    print("age < 5,price is $" + str(price))
elif age < 10:
    price = 5
    print("age < 5,price is $" + str(price))
else:
    price = 10
    print("age < 5,price is $" + str(price))

#检查多个条件
age = 10
money = 10000
'''
ccc
ddd
'''
if age < 5 and money < 10001:
    print('aaa')
if age < 10 and money < 10000:
    print('bbb')
if age < 20 and money < 10001:
    print('ccc')
if age < 5 or money < 10001:
    print('ddd')

'''
add MUSHROOMS
sorry,we are out of green peppers right now.
add EXTRA CHEESE
finished making your pizza
'''
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('sorry,we are out of green peppers right now.')
    else:
        print('add ' + requested_topping.upper())
print('finished making your pizza')
#检查元素是否在列表中
'''
green peppers in requested_toppings
apple is not in requested_toppings
'''
if 'green peppers' in requested_toppings:
    print('green peppers in requested_toppings')
if 'apple' not in requested_toppings:
    print('apple is not in requested_toppings')

#打印空列表
m_list = []
#无任何输出
for i in m_list:
    print(i)
#打印前应先判断是否为空
#m_list is empty
if m_list:
    for i in m_list:
        print(i)
else:
    print('m_list is empty')


'''
Add MUSHROOMS
we don't haveFRENCH FRIES
Add EXTRA CHEESE
finished making your pizza
'''
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Add ' + requested_topping.upper())
    else:
        print("we don't have " + requested_topping.upper())
print('finished making your pizza')