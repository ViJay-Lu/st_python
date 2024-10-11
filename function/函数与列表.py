"""eg1:简单使用方式"""
def greet_user(users):
    """向列表中的每位用户都发出消息"""
    for name in users:
        msg = "Hello, " + name.title() + "!"
        print(msg)


_users = ['vijay','yoyo','lilian']
greet_user(_users)

"""eg2:修改列表"""
def mdf_users(unprinted_designs,completed_models):
    while unprinted_designs:
        completed_models.append(unprinted_designs.pop())

unp_de = ['yoyo','vijay']
com_md = []

mdf_users(unp_de,com_md)
for name in com_md:
    print(name)
print('========================')
# 0
print(len(unp_de))
# NULL
for name in unp_de:
    print(name)

print('------------------------')
"""禁止函数修改列表---传递切片"""
unp_de_new = ['yoyo','vijay']
com_md_new = []

mdf_users(unp_de_new[:],com_md_new)
for name in com_md_new:
    print('com_md_new value is:',name)

for name in unp_de_new:
    print('unp_de_new value is:',name)