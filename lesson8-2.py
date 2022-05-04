# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class MyZeDiEr(Exception): #класс MyZeDiEr ссылается на объект exeption
    def __init__(self, txt): # init-Конструктор в ООП - называется специальный метод, вызываемый при создании экземпляра класса.
        self.txt = txt # аттрибут класса-свойство


def div(s_1, s_2): #метод класса
    try: # создает исключение
        s_1, s_2 = int(s_1), int(s_2) # аттрибуты объета exeption
        if s_2 == 0:
            raise MyZeDiEr("Division by zero forbidden!!!") #raise - возбудить исключение.
        return round(s_1 / s_2, 3)# возврат числа от деления s_1 / s_2, округленного до 3 первых цифр
    except ValueError: #ValueError - функция получает аргумент правильного типа, но некорректного значения.
    #exept- перехватывает исключение
        return "Value Error" # врзвращает строку "Value Error"
    except MyZeDiEr as my:
        return my


print(div(input("Enter first number - "), input("Enter first second - ")))
# напечатай(divmod(x, y)	Пара (x // y, x % y), необходимо ввести 1 и 2 число


print('*' * 100)


class MyDivisionZeroError(Exception): # класс(объект)
    def __init__(self, txt): #init-Конструктор в ООП - называется специальный метод, вызываемый при создании экземпляра класса.
        # self-cсылается на объект
        self.txt = txt #аттрибут


div = lambda x, y: x / y if y != 0 else MyDivisionZeroError('Ошибка дедения на 0!!')
#divmod(x, y)	Пара (x // y, x % y)
#lambda- функция выполняющая обмен значений
# условие if не равно 0, иначе исключение

print(div(1, 0))

print(div(4, 2))