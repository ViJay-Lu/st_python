#int--->str str()
i=2
str1 = str(i)
#<class 'str'> 2
print(type(str1),str1)

#str--->int int("")
str2="1234"
i2=int(str2)
#<class 'int'> 1234
print(type(i2),i2)

#int--->float
float_num = float(1234)
#<class 'float'> 1234.0
print(type(float_num),float_num)


#float--->int
int_num = int(1234.123)
#<class 'int'> 1234
print(type(int_num),int_num)

#err int(),float() 只能传数字类型
'''
float_num1 = float("test")
print(type(float_num1),float_num1)
int_num1 = int("test")
print(type(int_num1),int_num1)
'''
