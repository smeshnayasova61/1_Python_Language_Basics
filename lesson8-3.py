# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка
# на наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
# пользователя данные и заполнять список необходимо только числами. Класс-исключение должен
# контролировать типы данных элементов списка. Примечание: длина списка не фиксирована. Элементы
# запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например,
# команду «stop». При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во
# время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
# Вносить его в список, только если введено число. Класс-исключение должен не позволить
# пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = [] # пустой список

while True: # цикл
    inp_data = input("Введите число: ")
    if inp_data == "": # если переменная inp_data = строке, выход из цила
        break
    try:
        if inp_data.replace("-", "").replace(".", "").isdigit(): # isdigit- стр состоит из цифирь, replace- поменять значения в стр
            my_list.append(float(inp_data)) # добавить в список вещественные (десятичные дроби) числа
        else:
            raise OwnError("введено не число") #raise - возбудить исключение.
    except OwnError as err: # выводит искл как err
        print(err) #напечатай err
        continue #продолжить

print(my_list) #напечатай список

print('*'*100)


import re # импорт модуля регулярных выражений


class NotNumeric(Exception): #класс(объект)
    def __init__(self, text): # init-Конструктор в ООП - называется специальный метод, вызываемый при создании экземпляра класса.
        self.text = text #аттрибут класса


num = re.compile(r'^[-+]?\d+[,.]?\d*$') #объект
#re.compile(pattern, repl, string)-Мы можем собрать регулярное выражение в отдельный объект, который может быть использован для поиска
#r''-перевод курсора на начало строки после завершения работы со стр
result = [] #результат записать в пустой список

while True:
    try:
        el = input('Введите элемент списка(число): ')
        if el.lower() == 'stop':
            break
        elif num.match(el):
            result.append(el)
        else:
            raise NotNumeric('Число число')
    except NotNumeric as err:
        print(err)
print(result)


print('*'*100)

class MyList:
    print_list = []

    # Попробуем сделать исключение как класс в классе..
    @staticmethod
    class NotFloatExcept(Exception):
        def __init__(self, txt):
            self.txt = txt

    # Проверим что вновь введенная строка является числом, если да, перобразуем к числовому типу
    def __is_float(self, input_str):
        is_one_dot, is_one_minus = 0, 0
        for i in input_str:
            if ord(i) >= 48 and ord(i) <= 57:
                pass
            # В числе может быть одн точка
            elif ord(i) == 46 and is_one_dot == 0:
                is_one_dot += 1
            # А еще минус
            elif ord(i) == 45 and is_one_minus == 0:
                is_one_minus += 1
            else:
                raise self.NotFloatExcept('Введенная строка не является числом!')

        #  Если число целое, так и вернем
        if is_one_minus == 1 and len(input_str) == 2:
            return int(input_str)
        elif is_one_minus == 1:
            raise self.NotFloatExcept('Введенная строка не является числом!')
        elif is_one_dot == 0:
            return int(input_str)
        return float(input_str)

    # Добавляем новое число в список
    def __call__(self, new_str): #__call__() — срабатывает при обращении к экземпляру класса как к функции,
        try:
            self.print_list.append(self.__is_float(new_str))
        except self.NotFloatExcept as e:
            print(e)

    # Выводим на печать
    def __str__(self): #__str__() — срабатывает при передаче объекта функциям str() и print(), преобразует объект к строке,

        return str(self.print_list)[1:-1]


list = MyList()

while True:
    print('Введите число: ', end='')
    n = input()
    if n == '':
        print('Окончание программы')
        break
    else:
        list(n)
        print(list)
