import json

def get_stored_username():
    file_name = 'user_info.json'
    try:
        with open(file_name) as f:
            username = json.load(f)
    #如果文件为空，则抛异常在此处理
    except json.decoder.JSONDecodeError:
        return None
    except FileNotFoundError:
        return None
    else:
        return username

def add_new_username():
    file_name = 'user_info.json'
    with open(file_name, 'w') as file_object:
        new_username = input('Enter new username: ')
        json.dump(new_username, file_object)
    return new_username


def greet_user():
    username = get_stored_username()
    if username:
        print('welcome back,' + username + '!')
    else:
        username = add_new_username()
        print('welcome, ' + username + '!')

greet_user()

