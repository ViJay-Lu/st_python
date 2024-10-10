#此方法，运行目录以及文件中均不能有中文，否则会报错
#在当前路径找文件
with open("test_file.txt") as f:
    contents = f.read()
    print(contents)

#相对路径找文件
#此处的\\,是转义字符。
# 否则\C处会警告：SyntaxWarning: invalid escape sequence '\C'
# \t直接报错，被认为是制表符。这样就找不到对应的目录文件

with open('..\\Chapter_9_class\\test_file.txt') as file_object:
    contents = file_object.read()
    print(contents)