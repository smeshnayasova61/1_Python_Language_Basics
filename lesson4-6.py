#6. Реализовать два небольших скрипта: ● итератор,
# генерирующий целые числа, начиная с указанного; ● итератор,
# повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля
# itertools. Обратите внимание, что создаваемый цикл не должен
# быть бесконечным. Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл. Вторым пунктом
# необходимо предусмотреть условие, при котором повторение
# элементов списка прекратится.
# посмотрела как решается задача

from  itertools import  count, cycle
print('Программа генерирует целые числа, начиная с указанного. Для генерации следующего цисла необходимо нажать Enter, для выхода из программы "q"')
for i in count(int(input('Введите стартовое число: '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break
print('Программа повторяет элементы списка. Для генерации следующего повторения необходимо нажать Enter, для выхода из программы - "q"')
u_list = input('Введите список, разделяя элементы пробелом: ').split()
iter = cycle(u_list)
quit = None
while quit != 'q':
    print(next(iter), end='')
    quit = input()

print('*'*100)

from itertools import  count, cycle
my_count = count(7)
my_cycle = cycle('ABC')
for _ in range(5):
    print("(my_count, my_cycle) = ({},{})".format(next(my_count), next(my_cycle)))

print('*'*100)

from itertools import  islice, count, cycle
def unexpected(start_el, stop_el, num_str):
    try:
        start_el, stop_el, num_str = int(start_el), int(stop_el), int(num_str)
        my_list = [el for el in islice(count(), start_el, stop_el + 1)]
        #repeat_list = [el for el in islice(cycle(my_list), num_str)]
        r_list = iter(el for el in cycle(my_list))
        repeat_list = [next(r_list) for _ in range(num_str)]
        print(my_list)
        return repeat_list
    except ValueError:
        return "Value Error"
    except TypeError:
        return "TypeError"
print(unexpected(input('List starting at - '), input('from to - '), input('Number of repetition - ')))

print('*'*100)
#a)
from itertools import  count, cycle
iterator = count(int(input('введите целое число, начиная с которого будут генерироваться числа: ')))
print('первые 10 чисел начиная с введенного вами числа: ')
for i in range(10):
    print(next(iterator), end=' ')
#b)
print('\n- cycle -')
lst = ['String', 101,3.1415, 15.457]
iterator = cycle(lst)
# перебираем элементы списка 2 раза
for in range(len(lst)*2):
    print(next(iterator), end='')





