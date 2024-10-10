#try-except-else语法

while True:
    first_num = input('input first_num:')
    if first_num == 'q':
        break
    second_num = input('input second_num:')
    try:
        answer = int(first_num)/int(second_num)
    except ZeroDivisionError:
        print("you can't divide by zero")
    except NameError:
        print("input num err,try again")
    except ValueError:
        print("input num err,try again")
    else:
        print(answer)