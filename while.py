num = 1
#eg1:
'''
while num <= 10:
    print(num)
    num += 1
    if num == 5:
        print('==============')
'''

#eg2:
flag = True
'''
while flag:
    print(num)
    num +=1
    if num == 15:
        flag = False
'''

#eg3

while flag:
    input_msg = input('please input message: ')
    message = input_msg
    if message == 'exit':
        print(message)
        flag = False
    elif message == "":
        print('message is NULL,please try again')
    else:
        print('input message is :',message)

