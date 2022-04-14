#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

str = input('Введите строку из нескольких слов, разделенных пробелами: ').split()
print(type(str)) # list
print('\n'.join(str)) # перевели list в str и вывели каждое слово с новой строки.

for id, val in enumerate(str):
    if 0 <= len(val) <= 10:
        id+=1
        print(id, val)
    else:
        print('Уменьшить слово до 10 символов')

print ('*' * 100)

my_str = input('Введите строку из нескольких слов, разделенных пробелами: ').split()
for id, val in enumerate(my_str, 1):
    if 0 <= len(val) <= 10:
        print(id, val)
    else:
        print('Уменьшить слово до 10 символов')

print ('*' * 100)

s = input('Введите несколько слов через пробел: ').split()
for n, i in enumerate(s, 1):
    print(f'{n}) {i:.10}')

print ('*' * 100)

my_string = input('Введите несколько слов через пробел: ').split()
for i, world in enumerate(my_string, 1):
    print(f'{i}. {world[:10]}')












