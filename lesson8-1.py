# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором
# @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например,
# месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

# 2- объекты: число месяц год. Как и когда их записывать?
# 1- класс дата
# 3- конструктор-today в виде строки день-месяц=год
# 4- метод1 с декоратором  @classmethod, извлекает чч, мм, гг и преобразовать их к типу число???
# 5- метод2 @staticmethod -проводит валидацию числа, месяца и года???


class Number(int): #класс Number в виде числа
    def __str__(self):  # фукция-конструктор принимает число в виде стр, с self, которая связывается с объектом класса
        # — срабатывает при передаче объекта функциям str() и print(), преобразует объект к строке
        return f"{self:02}" # возвращает отформатированную строку состоящую из числа

class Date: # класс Date
    date_attrs = ('day', 'month', 'year') #атрибуты(свойства) класса даты = день, месяц, год

    def __init__(self, date: str, /): #init-конструктор-спец метод при создании экземпляра класса, self- ссылка на объект
        day, month, year = self.transform(date.split('-')) # атрибуты экземпляра(объекта)

        if not self.validate(day, month, year): # условие проверки: верный ли формат даты
            raise ValueError(f"{date} invalid date format") #Valueerror-функция получает аргумент с недопустимым присвоенным ей значением
            #raise - генерирует\инициирует исключение
        self.day = day #атрибут объекта
        self.month = month #атрибут объекта
        self.year = year #атрибут объекта

    def __iter__(self): #метод возвращает итератор для контейнера.
        for attr in self.date_attrs: #цикл ищет переменную attr в объекте date_attrs (перебирает 'day', 'month', 'year')
            yield self.__getattribute__(attr) #__getattr__(self, name) - вызывается, когда атрибут экземпляра класса не найден в обычных местах (например, у экземпляра нет метода с таким названием)
            # yield - определение функции-генератора.

    @classmethod #Таким декоратором дополняется метод, который получает класс в качестве первого аргумента.
    #Черезclsмы обращаемся к методу класса, ачерезself— к экземпляру класса (объекту).
    def transform(cls, date): #метод transform, 1 аргумент cls, 2 - date
        return [Number(i) for i in date] #нерни число с переменной i, i ищи в  классе date

    @staticmethod #Статические методы имеют доступ только к атрибутам классов, к ним нельзя обратиться через self. По сути, статические методы ничего не знают ни о классе, ни об экземпляре, на который вызываются.
    #методы, которые вызываются напрямую через имя класса (статические методы).
    def validate(*date):
        if not all(map(lambda x: isinstance(x, int), date)): #isinstance(object, ClassInfo) - Истина, если объект является экземпляром ClassInfo или его подклассом. Если объект не является объектом данного типа, функция всегда возвращает ложь.
            #map(function, iterator) - Итератор, получившийся после применения к каждому элементу последовательности функции function.
            #Анонимные функции создаются с помощью инструкции lambda.
            #all(последовательность) - Возвращает True, если все элементы истинные (или, если последовательность пуста)
            return False

        day, month, year = date #аттрибуты класса Data
        return all([1 <= day <= 31, 1 <= month <= 12, year >= 1970])

    def __str__(self):
        return f"Date is '{'.'.join([str(s) for s in self])}'"


if __name__ == '__main__':
    try:
        print(Date('31-12-2022'))
        print(Date('41-01-1970'))
    except ValueError as e:
        print(e)

print('*' * 100)

class OwnError(Exception): #класс свой исключения
    def __init__(self, txt):
        self.txt = txt


class Date(object): #класс
    def __init__(self, day=0, month=0, year=0): #метод __init__ перегружает конструктор класса. Конструктор - создание экземпляра класса.
        self.day = day #атрибут объекта(экземляра)
        self.month = month
        self.year = year

    @classmethod #Таким декоратором дополняется метод, который получает класс в качестве первого аргумента.
    def from_string(cls, date_as_string): #метод
        is_date = cls.is_date_valid(date_as_string)
        try:
            if is_date == False:
                raise OwnError("Wrong date!") #создаем свое ислючение
        except OwnError as err:
            print(err)
            return

        day, month, year = map(int, date_as_string.split('-')) #объекты\экземпляры
        # map(function, iterator) - Итератор, получившийся после применения к каждому элементу последовательности функции function.
        #дату приводим из стр к числу
        date1 = cls(day, month, year)
        return date1

    @staticmethod #методы, которые вызываются напрямую через имя класса (статические методы)
    def is_date_valid(date_as_string): #метод (действие, которое совершает объект), проводим валидацию аттрибутов класса
        day, month, year = map(int, date_as_string.split('-')) #аттрибуты приводим из стр к числу
        return day <= 31 and month <= 12 and year <= 3999


date2 = Date.from_string('11-10-2012') #объект класса с реальными данными

try:
    print(date2.day, date2.month, date2.year)
except:
    print('OOps. Something wrong')

print('*' * 100)

class Data:
    def __init__(self, data): #init-конструктор-спец метод при создании экземпляра класса, self- ссылка на объект
        self.data = data #аттрибут-свойство класса

    @classmethod #Таким декоратором дополняется метод, который получает класс в качестве первого аргумента.
    def change_type(cls, data): #метод(изменение_типа (1 аргумент-cls, 2 аргумент- data)
        return f'День {int(data[0]):02d}, Месяц {int(data[1]):02d}, Год {int(data[2])}'
        # возвращаем: аттрибуты класса в виде форматированной строки с цифирями

    @staticmethod #методы, которые вызываются напрямую через имя класса (статические методы)к аттрибутам
    def validation(data): #метод класса, позволяюший првести валидацию в аттрибутах класса
        if not int(data[0]) in range(1, 32) or not int(data[1]) in range(1, 13) or int(data[2]) > 2020:
            return 'Введена некоррекная дата!'

    def data_func(self): #метод
        result_1 = Data.change_type(self.data.split('-'))
        result_2 = Data.validation(self.data.split('-'))
        return result_2 if result_2 else f'Переформатированная дата (тип int)\n{result_1}'


user_data = input('Введите дату (чч-мм-гг): ') #объект
mc = Data(user_data) #объект
print(mc.data_func()) #распечатай объект через который осуществляется вызов метода
user_data = input('Введите дату (чч-мм-гг): ') #объект
mc_2 = Data(user_data)#объект
print(mc_2.data_func()) #распечатай объект через который осуществляется вызов метода
print(mc.data_func()) #распечатай объект через который осуществляется вызов метода
