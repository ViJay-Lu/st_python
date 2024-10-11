dimensions = (200,50)
'''
(200, 50) <class 'tuple'>
200
50
'''
print('old dimensions:',dimensions,type(dimensions))
print(dimensions[0])
print(dimensions[1])
#修改元组变量
'''
元组元素的值不能修改
#TypeError: 'tuple' object does not support item assignment
dimensions[0] = 250
print(dimensions[0])
'''
#虽然不能修改元组元素值。但是可以给存储元组的变量重新赋值
dimensions = (250,50)
print('new dimensions:',dimensions) #new dimensions: (250, 50)

#遍历元组
for i in dimensions:
    print(i)