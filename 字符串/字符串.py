#知识点1：大小写转换
_str = 'hello'
_str1 = _str.title()
_str2 = _str.upper()
_str3 = _str2.lower()
#print(' _str1 = ',_str1,'\n _str2 = ',_str2,'\n _str3 = ',_str3)

#知识点2：格式化输出字符串
first_name = 'lu'
last_name  = 'yoyo'
#eg1:python3.6以上版本引入f
full_name = f"{first_name}{last_name}"
print("full_name is ", full_name) #luyoyo
#eg2:
full_name = f"Hello,my name is {first_name.title()}{last_name.upper()}"
print(full_name) #Hello,my name is LuYOYO
#eg3:以下版本使用format
full_name = "Hello,my name is {}{}".format(first_name.title(), last_name)
print(full_name)

#知识点3：制表符、换行符
_str4 = '\nhello\tpython  ha '
print(len(_str4),'\n',_str4)

#知识点4：去空格
_str5 = " hi python  "
#rstrip去末尾空格是暂时的，再次查看_str5时候，末尾还是有空格
print(len(_str5.rstrip()),len(_str5)) #10 12 末尾有两空格
#永久删除末尾空格
_str5 = _str5.rstrip()
print(_str5,len(_str5)) #len = 10

#去掉开头空格
_str5 = "  hi vijay"
print(_str5.lstrip(),len(_str5),len(_str5.lstrip())) #hi vijay 10 8
#lstrip和rstrip一样，不会永久删除
_str5 = _str5.lstrip()
print(_str5,len(_str5))

#去掉开头和末尾空格
_str6 = "  hi py  "
print(_str6.strip(),len(_str6)) #9
_str6 = _str6.strip()
print(_str6,len(_str6)) #5