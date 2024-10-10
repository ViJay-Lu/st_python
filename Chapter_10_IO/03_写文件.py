file_name = 'test_file1.txt'

#w：如果文件存在则清空文件，不存在则创建.
#with open(file_name, 'w') as file_object:

#r+.读取和写入。写入时，会从头覆盖文件.
#with open(file_name, 'r+') as file_object:

#从后追加
with open(file_name, 'a') as file_object:
    file_object.write('8')
    file_object.close()

with open(file_name, 'r') as file_object:
    for line in open(file_name):
        print(line)