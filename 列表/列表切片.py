m_family = ['vijay','lilian','yoyo','mm','dd','sister']
#输出的也是一个列表
print(m_family[0:3]) #['vijay', 'lilian', 'yoyo']
print(m_family[3:]) #['mm', 'dd', 'sister']
print(m_family[-2:]) #['dd', 'sister']
print(m_family[3:-1]) #['mm', 'dd']
print(m_family[:]) #['vijay', 'lilian', 'yoyo', 'mm', 'dd', 'sister']

#遍历切片
'''
Vijay
Lilian
Yoyo
'''
for name in m_family[0:3]:
    print(name.title())

#复制列表
my_foods = ['pizza','falafel','carrot cake']
#提取切片，创建副本，将my_foods副本存储到friend_foods中
friend_foods = my_foods[:]
print('my favourite foods are:')
print(my_foods) #['pizza', 'falafel', 'carrot cake']
print("\nMy friend's favourite foods are:")
print(friend_foods) #['pizza', 'falafel', 'carrot cake']
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods) #['pizza', 'falafel', 'carrot cake', 'cannoli']
print(friend_foods) #['pizza', 'falafel', 'carrot cake', 'ice cream']

#错误方法
my_foods = ['pizza','falafel','carrot cake']
#friend_foods，my_foods指向同一块内存
#将新变量friend_foods 关联到包含在my_foods 中的列表，因此这两个变量都指向同一个列表
friend_foods = my_foods
print('\nMy favourite foods are:')
print(my_foods) #['pizza', 'falafel', 'carrot cake']
print("My friend's favourite foods are:")
print(friend_foods) #['pizza', 'falafel', 'carrot cake']
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods) #['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print(friend_foods) #['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']