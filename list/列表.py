#python中用[]表示列表,类型为:list
names = ['vijay','yoyo',2,'lilian']
print(names,type(names))

#访问列表元素
name1 = names[0].title()
print(name1,type(name1))
name2 = names[-1].upper() #-1:最后一个元素
print(name2,type(name2))
message = f'my name is {names[0].upper()},my daughter name is {names[1].title()}'
print(message)

#列表元素增、删、改
names[2] = 'modify'
print(names)
#add
names.append('luweijie')
print(names)
names.insert(0,'lujinyue')
print(names,names[-1])
names.insert(6,'liminlian')
print(names)
#delete
#eg1：del删除的元素不能使用
del names[3] #delete 'modify'
print(names)
#eg2：pop,列表类似于栈，pop为弹出栈顶元素,可以直接使用
name = names.pop()
print(names)
#pop也可以支持下标操作
names.pop(-2)
print(names)
#根据“值”删除
names.remove('vijay')

#列表排序

'''
重点标注：
    sort()是方法，调用方法为list.sort()
    sorted()是函数，调用方法为sorted(list)
'''

cars = ['bmw','toyota','audi','subaru']
print(cars) #['bmw', 'toyota', 'audi', 'subaru']
#sort方法为永久排序，列表不可恢复到最初的排序
cars.sort()
print(cars) #['audi', 'bmw', 'subaru', 'toyota']
#反向排序,永久
cars.sort(reverse=True)
print(cars) #['toyota', 'subaru', 'bmw', 'audi']
#临时排序
cars = ['bmw','toyota','audi','subaru']
print(sorted(cars)) #['audi', 'bmw', 'subaru', 'toyota']
print(cars) #['bmw', 'toyota', 'audi', 'subaru']
print(sorted(cars,reverse=True)) #['toyota', 'subaru', 'bmw', 'audi']
new_cars = sorted(cars)
print(new_cars) #['audi', 'bmw', 'subaru', 'toyota']

#翻转列表
cars = ['bmw','toyota','audi','subaru']
cars.reverse() #['subaru', 'audi', 'toyota', 'bmw']
print(cars)

#获取列表长度
cars_len = len(cars)
print(cars_len) #4

#下标访问不可越界，否则报错
#err max=3,[0,1,2,3]
#car = cars[4]
#cars1 = []
#print(cars1[-1])

#列表打印
cars = ['bmw','toyota','audi','subaru']
#eg1:for循环
for car in cars:
    print(car)

#eg2
for car in cars:
    print(car.upper() + ",that was a great car")
    print("i want have this ",car.title(),'\n')

#创建数值列表
for num in range(1,5):
    print(num)

num_list = list(range(1,4))
print(num_list)