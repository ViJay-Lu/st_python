alien = {'color':'green'}
print(alien,type(alien)) #{'color': 'green'} <class 'dict'>
print(alien['color']) #green
#err 不支持下标访问
#print(alien[0])

alien = {'color':'green','point':5}
new_point = alien['point']
print('you just earned '+ str(new_point) + ' points')
print(alien) #{'color': 'green', 'point': 5}
#添加键值对
alien['speed'] = 'slow'
alien['x_position'] = 5
alien['y_position'] = 10
#{'color': 'green', 'point': 5, 'speed': 'slow', 'x_position': 5, 'y_position': 10}
print(alien)


if alien['speed'] == 'fast':
    x_increment = 1
elif alien['speed'] == 'slow':
    x_increment = 2
else:
    x_increment = 3
alien['x_position'] += x_increment
print(alien['x_position']) #7

#删除元素
del alien['x_position']
print(alien) #{'color': 'green', 'point': 5, 'speed': 'slow', 'y_position': 10}

favorite_languages = {
    'vijay' : 'python',
    'yoyo' : 'java',
    'lilian' : 'c'
}
#{'vijay': 'python', 'yoyo': 'java', 'lilian': 'c'}
print(favorite_languages)
#yoyo favorite language is JAVA
print('yoyo favorite language is',favorite_languages['yoyo'].upper())

#创建空字典
m_dict = {}
print(type(m_dict),m_dict)