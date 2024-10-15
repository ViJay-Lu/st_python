#eg1:简答返回值
def get_username(username):
    return username

m_str = get_username('vijay')
#type is str
print(m_str, '\n', type(m_str))

m_intger = get_username(123)
#type is int
print(m_intger, '\n', type(m_intger))

#eg2:
def get_full_name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

m_fullname = get_full_name('lu','vijay')
print(m_fullname,type(m_fullname))


#eg3:实参变可选
# def get_formatted_name(first_name,middle_name='',last_name)
# err 默认参数后不能跟非默认参数
def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return  full_name.title()

m_fullname = get_formatted_name('lu','jie','wei')
print(m_fullname)
m_fullname = get_formatted_name('lu','jinyue')
print(m_fullname)

#eg4:返回字典
def get_name(first_name,last_name,middle_name=''):
    fullname = {}
    if middle_name:
        fullname = {'first':first_name,'middle':middle_name,'last':last_name}
    else:
        fullname = {'first':first_name,'last':last_name}
    return fullname

print('=====================')
fullname = get_name('lu','jie','wei')
print(fullname,'\t',type(fullname))
print('-------------------')
for first_name, last_name in fullname.items():
    print(first_name,last_name)

fullname = get_name('lu','yoyo')
print(fullname,'\t',type(fullname))

#eg5:
def bulid_person(first_name,last_name,age):
    person = {'first_name':first_name,'last_name':last_name,'age':age}
    return person

person = bulid_person('lu','vijay',32)
print(person)
print('======')
for key,value in person.items():
    #打印出来的结果一模一样
    print(key,value)
    print(f'{key}:{value}')

print('=========')
#只打印first_name,last_name
for key in['first_name','last_name']:
    print(person[key])