#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3] #значения функции приводим к списку-list
    try:
        my_list.remove(min(my_list)) # так как функция может принять минимальное значение, что для нас является исключением, то надо удалить мин элемент из списка
        return sum(my_list) #вернуть сумму чисел в переменной my_list без минимального значения
    except TypeError: # водим конструкцию try-except для вывода min значения
        return "Вводить только числа: " # без минимального значения
print(my_func(2, 11, -30))

print('*'*100)

def my_func(arg1, arg2, arg3):
    return sum(sorted([arg1, arg2, arg3])[1:]) #сортировка от мин к макс и срез от 1 элемента до конца, веонем сумму среза
print(my_func(1978, 1, 2))

print('*'*100)

#def my_func(arg1, arg2, arg3):
#    my_func = lambda arg_1, arg_2, arg_3: (arg_1 + arg_2 + arg_3) - min(arg_1 + arg_2 + arg_3)
#print(my_func(7, 8, 9))



