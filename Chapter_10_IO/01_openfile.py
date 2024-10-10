#此方法，运行目录以及文件中均不能有中文，否则会报错
#在当前路径找文件
with open("test_file.txt") as f:
    contents = f.read()
    print(contents)

#相对路径找文件
#此处的\\,是转义字符。
# 否则\C处会警告：SyntaxWarning: invalid escape sequence '\C' (无效的转义序列)
# \t直接报错，被认为是制表符。这样就找不到对应的目录文件

# 另外需要注意的是，Windows下，为反斜杠'\',Linux或者macos,路径为'/'
with open('..\\Chapter_9_class\\test_file.txt') as file_object:
    contents = file_object.read()
    print(contents)


# 方式三：将路径存储在变量中
file_path = 'E:\\workspace\py\\vijay\Chapter_10_IO\\test_file.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)