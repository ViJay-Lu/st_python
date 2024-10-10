file_name = 'test_file.txt'

#这样打印每行之间会对一个空格，因为每行都有换行符。所有可以用 line.rstrip()打印
with open(file_name, 'r') as file_object:
    for line in file_object:
        print(line)

print("============================")
#创建保存每一行数据的列表
#readlines()方法从文件中读取每一行，并存储在列表中
with open(file_name, 'r') as file_object:
    lines = file_object.readlines()

file_str = ''
for line in lines:
    file_str += line.strip()
print(file_str)

user_name = input('please enter your name: ')

if user_name in file_str:
    print('file have your name')
else:
    print('file do not have your name')


