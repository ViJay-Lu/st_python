'''
message = input('请输入一个数字：')
print('这个数字是：' + str(message))
'''

age = input('please input your age: ')
age = int(age)
if 0 < age <= 10:
    print('age <= 10')
elif 11 < age < 21:
    print('age < 20')
else:
    print('age > 20')