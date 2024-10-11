vijay = {
    'first_name':'lu',
    'last_name':'weijie',
    'age':32,
    'weight':70
}
'''
key: First_Name
value: lu
key: Last_Name
value: weijie
key: Age
value: 32
key: Weight
value: 70
'''
for key,value in vijay.items():
    print('key:',key.title())
    print('value:',value)
print('---------------------------------')
'''
key: First_Name
key: Last_Name
key: Age
key: Weight
'''
for key in vijay.keys():
    print('key:',key.title())
print('-------------------------------------')
#等价于上方写法，因为字典默认是key遍历
for key in vijay:
    print('key:',key.upper())
'''
value: lu
value: weijie
value: 32
value: 70
'''
for value in vijay.values():
    print('value:',value)
print('-------------------------')
#根据key排序输出
'''
key: Age
key: First_Name
key: Last_Name
key: Weight
'''
for key in sorted(vijay.keys()):
    print('key:',key.title())

if 'num' not in vijay.keys():
    print('no num') #no num

print('---------------------------------------')
favorite_languages = {
    'vijay' : 'python',
    'yoyo' : 'java',
    'lilian' : 'c',
    'sister' : 'python'
}

'''
有重复项，当数据量大时，不好统计总共有多少值
value: C
value: Java
value: Python
value: Python
'''
for value in sorted(favorite_languages.values()):
    print('value:',value.title())
print('-------------------------------')
'''
set()方法可以去重
value: Java
value: C
value: Python
'''
for value in set(sorted(favorite_languages.values())):
    print('value:',value.title())