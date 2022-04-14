#6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с
# параметрами, то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
#Пример готовой структуры:
#[
#(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#]
#Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.
#Пример:
#{
#“название”: [“компьютер”, “принтер”, “сканер”],
#“цена”: [20000, 6000, 2000],
#“количество”: [5, 2, 7],
#“ед”: [“шт.”]
#}
goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''} # КОРТЕЖ
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []} # КОРТЕЖ
num = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q': # для выхода из цикла или продолжения
        break
    num +=1 #key кортежа
    f_copy = features.copy() # переменная f_copy = скопированное выражение из переменной features
    for f in features: # поиск переменной f  в содержимом переменной features
        pro = input(f'Введите значение свойства "{f}": ') #ввод свойства "название"
        f_copy[f] = int(pro) if f in 'цена количество' and pro.isdigit() else pro #меняем тип числовых свойства
        analytics[f].append(f_copy[f]) #добавляем свойство в аналитику
    goods.append((num, f_copy)) #добавляем свойство в список товаров
    print(f'\nСтруктура товаров\n{goods}')
    print(f'\n Текущая аналитика по товарам: \n {"*" * 30}')
    for key, value in analytics.items():
        print(f'{key:>30}: {value}')
    print("*" * 30)
