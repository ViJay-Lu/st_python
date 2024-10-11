from name_function import get_full_name

while True:
    first_name = input('Enter your first name: ')
    if first_name == 'q':
        break
    last_name = input('Enter your last name: ')
    if last_name == 'q':
        break
    full_name = get_full_name(first_name, last_name)
    print(full_name)