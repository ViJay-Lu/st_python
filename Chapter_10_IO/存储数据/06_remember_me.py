import json

file_name = 'user_info.json'

try:
    with open(file_name) as f:
        username = json.loads(f)
except FileNotFoundError:
    username = input('please enter your username: ')
    with open(file_name,'w') as f:
        json.dump(username,f)
        print("we'll remember you when you come back," + username)
else:
    print("welcome back," + username)
