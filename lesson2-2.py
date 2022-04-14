#2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input
a = [int(i) for i in input('Ведите список, состоящий  из цифр через пробел: ').split()]
for i in range(1, len(a), 2):
    #print(i)
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a])) #приведение списка к строке.

print('-' *100)

a = [i for i in input('Ведите список, состоящий  из букв через пробел: ').split()]
for i in range(1, len(a), 2):
    #print(i) #шаг индекса
    a[i - 1], a[i] = a[i], a[i - 1] #обмен значений элементов списка по индексу
print(a)

print('-' *100)

my_list = list(input('Ведите список, состоящий  из цифр через пробел: '))
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
    print (my_list)

print('-' *100)

my_list = input('Ведите список, состоящий  из цифирь через пробел: ').split()
print('Введенный список: ', my_list)
idx = len(my_list) if len(my_list) % 2 ==0 else len(my_list)-1
my_list[:idx:2], my_list[1:idx:2] = my_list[1:idx:2], my_list[:idx:2]
print('Измененный список: ', my_list)

print('-' *100)

user_list = input ('Введите числа через пробел: ').split()
for i in range(1, len(user_list), 2):
    user_list.insert(i-1, user_list.pop(i))
    print (user_list)

