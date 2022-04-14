#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

result_list = ['черная кошка', 573, 45.9, None]
print(result_list)
print(type(result_list))
print(type(result_list[0]))
print(type(result_list[1]))
print(type(result_list[2]))
print(type(result_list[3]))

print('*'*100)

my_list = [1, 1.2, (1+2j), 'my_str', [1, 'str', None], (1, 'str', None), {1, 'str', None, False},
           {"key_1":500,2:400,"key_3":True,4:None}, bool(20), b'text', bytearray(b'some text'), None, TypeError,
           zip(*[('a', 'b'), ('c', 'd'), ('e', 'f')]), range (1,10,2)]
for i, item in enumerate(my_list,1):
    print(f"{i}) {item} - {type(item)}")