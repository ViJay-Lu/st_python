#打印结果：1-5
from turtledemo.rosette import mn_eck

for i in range(1,6):
    print('i =',i)

#创建数字列表
numbers = list(range(1,6))
#[1, 2, 3, 4, 5]
print(numbers)

#步长：，终值：20
numbers = list(range(1,20,3))
#[1, 4, 7, 10, 13, 16, 19]
print(numbers)

#创建值为1-10平方的列表
#eg1:基础方法创建
numbers = []
for num in range(1,11):
    numbers.append(num**2)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(numbers)

#eg2:列表解析方法创建
numbers1 = [val**2 for val in range(1,11)]
print('number1 is:',numbers1)

#列表最值以及总和：
#100 1 385
print(max(numbers),min(numbers),sum(numbers))

#4-3:使用一个for循环，打印1-20的数
for i in range(1,21):
    print(i)

#4-4:创建一个列表，其中包含数字1~1 000 000，再使用一个for 循环将这些数字打印出来
large_list = [val for val in range(1,1_000_001)]
#耗时较长，先屏蔽
'''
for num in large_list:
    print(num)
print(min(large_list),max(large_list),sum(large_list))
'''

#4-5:通过给函数range() 指定第三个参数来创建一个列表，其中包含1~20的奇数；
#    再使用一个for 循环将这些数字都打印出来
m_list = [val for val in range(1,20,2)]
for i in m_list:
    print(i)

#4-7 3的的倍倍数数 ：创建一个列表，其中包含3~30内能被3整除的数字；
#    再使用一个for 循环将这个列表中的数字都打印出来
m_list = [val for val in range(3,31,3)]
for i in m_list:
    print(i)

#将同一个数字乘三次称为立方。例如，在Python中，2的立方用2**3 表示。
# 请创建一个列表，其中包含前10个整数（即1~10）的立方，再使用一个for 循环将这些立方数都打印出来。
m_list = []
for i in range(1,11):
    m_list.append(i**3)
for num in m_list:
    print(num)

#使用列表解析生成一个列表，其中包含前10个整数的立方
m_list = [val**3 for val in range(1,11)]
#[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
print(m_list)