#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def div(*args):
    try:
        arg1 = int(input("Input dividend "))
        arg2 = int(input("Input divider "))
        res = arg1 / arg2 ##мы выполняем инструкцию, которая может породить исключение, если arg2=0, то возникает исключение
    except ValueError: #ValueError - функция получает аргумент правильного типа, но некорректного значения.
        return 'ValueError' #return- возвращаем результат
    except ZeroDivisionError: #в блоке except мы перехватываем исключения
        return "Wrong devider! You can't use zero as a devider"
    return res
    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Wrong number! Devider can't be null")
    '''
print(f'result  {div()}')

print('*'*100)

def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        div_num = s_1 / s_2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Division by zero forbidden!!!"
    return round(div_num, 4)
print(div(input("Enter first number - "), input("Enter second - ")))

print('*'*100)

def div(s_1, s_2):
    s_1, s_2 = int(s_1), int(s_2)
    div_num = s_1 / s_2
    if s_2 != 0:
        return round(div_num, 4)
    else:
        print("Wrong number! Devider can't be null")
print(div(input("Enter first number - "), input("Enter second - ")))






