#python中，除法不管能不能整除，结果都是float类型
#eg1:
num = 6/3
#float 2.0
print(num,type(num))
#eg2:
num = 3**3.0
print(num,type(num))

#0.30000000000000004 计算机内部操作，忽略即可
print(0.1+0.2)

#py3.6及以上版本
universe_int = 1_000_000_001
print(universe_int,type(universe_int)) #1000000001 <class 'int'>
universe_float = 1.000_000_2
print(universe_float,type(universe_float)) #1.0000002 <class 'float'>

#多个变量赋值
x,y,z = 1,2,3
print("x:",x,"y:",y,"z:",z)
#err
#x,y,z=1 不能跟C++类似写法

#常量
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS,type(MAX_CONNECTIONS))
MAX_CONNECTIONS = 1
print(MAX_CONNECTIONS)
