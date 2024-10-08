
def get_username(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name

while True:
    _first_name = input('please input your first name: ')
    if _first_name == 'q':
        break
    elif not _first_name or _first_name.isspace():
        print('first name is null,please try again')
        continue
    else:
        _first_name = _first_name.replace(' ', '')

    _last_name = input('please input your last name: ')
    if  _last_name == 'q':
        break
    elif not _last_name or _last_name.isspace():
        print('last name is null,please try again')
        continue
    else:
        _last_name = _last_name.replace(' ','')

    full_name = get_username(_first_name, _last_name)
    print(full_name)