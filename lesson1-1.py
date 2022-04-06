#1. Поработайте с переменными, создайте несколько,
# выведите на экран.
# Запросите у пользователя некоторые числа и строки
# и сохраните в переменные, затем выведите на экран.
print('Привет, меня зовут Сова, мне 1 год')
# у нас 2 переменные
name = 'Сова'
age = 1
# вывести строку вместе с переменной в терминал
print (name, age, sep=',')
name = 'имя'
# тип переменной
print(type(name))
birthday_year ='1999'
period = 20
age = int (birthday_year) + period
print(age)
print('-------')
result = input()
print('Пользователь ввел', result)
name = input('Ваше имя: ')
print('Привет', name)
age = int(input('Сколько вам лет?:'))
period = 10
age_period = age + period
print('Через', period, 'вам будет', age_period)

test