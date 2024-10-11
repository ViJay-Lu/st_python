#需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套
#eg1：字典列表: 类型为列表，每个元素为字典

alien1 = {'color':'green'}
alien2 = {'color':'red'}
alien3 = {'color':'black'}

alien_list = [alien1,alien2,alien3]
print(type(alien_list)) #<class 'list'>
print(alien_list) #[{'color': 'green'}, {'color': 'red'}, {'color': 'black'}]
print(type(alien_list[0])) #<class 'dict'>
'''
key: color ,value: green
key: color ,value: red
key: color ,value: black
'''
for alien in alien_list:
    for key, value in alien.items():
        print('key:',key,',value:', value)

#eg2:生成30个外星人
aliens = []
for alien_num in range(30):
    new_alien = {'color':'green', 'speed':'slow'}
    aliens.append(new_alien)
print('len:',len(aliens)) #30
#修改部分
for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['speed'] = 'fast'
        alien['color'] = 'red'
    elif alien['color'] == 'red':
        alien['speed'] = 'fast'
        alien['color'] = 'yellow'

print('--------------------------')
'''
{'color': 'red', 'speed': 'fast'}
{'color': 'red', 'speed': 'fast'}
{'color': 'red', 'speed': 'fast'}
{'color': 'red', 'speed': 'fast'}
{'color': 'red', 'speed': 'fast'}
'''
for alien in aliens[:5]:
    print(alien)


#eg2:列表字典
#字典中存储列表，类型为字典，元素类型为列表
print('==================================')
favorite_languages = {
    'vijay':['c','python'],
    'yoyo':['java','c#'],
    'lilian':['python']
}
'''
Vijay's favorite language are :
	C
	Python

Yoyo's favorite language are :
	Java
	C#

Lilian's favorite language are :
	Python
'''
for key,value in favorite_languages.items():
    print('\n' + key.title() +"'s favorite language are :")
    for language in value:
        print('\t' + language.title())


#eg3:字典嵌套字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
print('============================')
print(type(users))
for username,userinfo in users.items():
    print('\nusername: ',username.title())
    full_name = userinfo['first'] + ' ' + userinfo['last']
    location = userinfo['location']
    print('\tFull name: ',full_name.title())
    print('\tLocation: ',location.title())