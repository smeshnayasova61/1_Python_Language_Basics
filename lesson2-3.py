#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.
# зима-12, 1,2, 2   весна- 3,4,5   лето-6,7,8, осень-9,10,11

month = int(input('Введите целое число от 1 до 12: '))
if month == 1 or month == 2 or month == 12:
    print('зима')
elif month == 3 or month == 4 or month == 5:
    print('весна')
elif month == 6 or month == 7 or month == 8:
    print('лето')
elif month == 9 or month == 10 or month == 11:
    print('осень')
else:
    print('error')

print('*'*100)

month = int(input('Введите целое число от 1 до 12: '))
seasons = ['зима', 'весна', 'лето', 'осень', 'зима'] # список
if 1 <= month <= 2 or month == 12:

print(seasons[0]) #обращение к индексу list-списка
elif 3 <= month <= 5:
    print(seasons[1])
elif 6 <= month <= 8:
    print(seasons[3])
elif 9 <= month <= 11:
    print(seasons[4])
else: print('error')

print('*' * 100)

month = int(input('Введите целое число от 1 до 12: '))
seasons = {1:'весна', 2:'лето', 3:'осень', 4:'зима'} # словарь-dictionary {ключ: значение}
if 1 <= month <= 12:
    print(seasons[month//3]) # обращение к ключу словаря (ключ=месяц целочисленное деление на 3)
else: print('error')

print('*' * 100)

month = int(input('Введите месяц года от 1 до 12: '))
month_dict = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель',5: 'май',6: 'июнь',7: 'июль',8: 'август',9: 'сентябрь',10: 'октябрь',11: 'ноябрь',12:'декабрь'}
month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
if month in month_dict:
    print(f'{month}-й месяц года - это {month_dict[month]}') #month -ключ
    print(f'{month}-й месяц года - это {month_list[month - 1]}') #month-1 - индекс
else:
    print('Неправильный номер.')

print('*' * 100)

saeson_dict = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
month_num = int(input('Введите номер месяца: '))
if month_num in sum(saeson_dict.values(), []): # сумма списков, формируется в один список -list
    for i in saeson_dict.items():
        if month_num in i[1]: # 1-индекс в новом list? который получен из суммы списков в словаре season_dict
            print(i[0])
            break

print('*' * 100)

while True:
    user_month = input('Введите номер месяца от 1 до 12: ')
    if user_month.isdigit() and 0 < int(user_month) <= 12:
        season_1 = ['зима', 'весна', 'лето', 'осень', 'зима'] #list-список
        season_2 = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'} #dictionary - словарь
        print(f'Список сезонов - {season_1[int(user_month)//3]}\nСловарь сезонов - {season_2[int(user_month)//3]}')
        break
    else:
        print('error')


