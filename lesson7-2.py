# 2. Реализовать проект расчёта суммарного расхода ткани на
# производство одежды. Основная сущность (класс) этого проекта — одежда, которая
# может иметь определённое название. К типам одежды в этом проекте относятся пальто
# и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост
# (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для
# пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на
# реальных данных. Реализовать общий подсчет расхода ткани. Проверить на практике
# полученные на этом уроке знания: реализовать абстрактные классы для основных
# классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC): # класс Clothes- потомок от ABC
    result = 0

    def __init__(self, param): #конструктор у родителя должен получать значение, потомок не забудет ввести значение
        self.param = param

    @property #декоратор
    @abstractmethod # декоратор
    def consumption(self): #декоратор следит за переопределением
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Costume(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return  f"{res}"

class Coat(Clothes):
    @property #декоратор для обращения для взаимодействия с методом как с атрибутом, т.е. без скобок
    def consumption(self):
        return round(self.param / 6.5) + 0.5

class Costume(Clothes):
    @property
    def consumption(self):
        return round((2 * self.param + 0.3) / 100) #метод -это формула

coat = Coat(42) #объкт
costume = Costume(178) #объкт
print(coat + costume + coat)

print('*'*100)

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self): #через конструктор инит взаимодействуем с родительским классом, даже если он пустой, мы в него все равно что то добавим
        pass

    @property
    @abstractmethod
    def raschet(self):
        pass

    def __add__(self, other):
        return self.raschet + other.raschet

class Coat(Clothes):
    def __init__(self, size): #через конструктор инит взаимодействуем с родительским классом, даже если он пустой, мы в него все равно что то добавим
        super().__init__()
        self.size = size

    @property #атрибут объекта size, оборачиваем его декоратором
    def size(self):
        return self.__size #возвращает в приватном режиме

    @size.setter #делаем метод size с декоратором setter
    def size(self, size):
        if size < 40:
            print('На детей не шьем. Начнем с сорокового.')
            self.__size = 40
        elif size > 58:
            print('Не многовато ли? 58 - максимум, для него и посчитаем')
            self.__size = 58
        else:
            self.__size = size

    @property
    def raschet(self):
        return self.__size / 6.5 + 0.5

class Costume(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 100:
            print('На детей не шьем.')
            self.__height = 150
        elif height > 240:
            print('Не многовато ли? 240 - максимум, для него и посчитаем')
            self.__height = 240
        else:
            self.__height = height

    @property
    def raschet(self):
        return 2 * (self.__height / 100) + 0.3

coat_1 = Coat(int(input('Введите размер пальто для расчета: ')))
print(f'Вам потребуется {coat_1.raschet: 2f} метров ткани на пальто {coat_1.size} размера')
costume_1 = Costume(int(input('Введите рост для костюма для расчета(в метрах)')))
print(f'Вам потребуется {costume_1.raschet: 2f} метров ткани на костюм {costume_1.height} роста ')

print('*'*100)

from abc import ABC, abstractmethod

class Clothes (ABC):
    instance = []

    def __init__(self, param):
        self.param = param
        Clothes.instances.append(self)

    @abstractmethod
    def cloth_consumption(self):
        pass

    def __del__(self):
        if self in Clothes.instances:
            Clothes.instances.remove(self)

class Coat(Clothes):
    @property
    def cloth_consumption(self):
        return round(self.param / 6.5 + 0.5, 2)

class Costume(Clothes):
    @property
    def cloth_consumption(self):
        return round((self.param * 2 + 0.3) / 100, 2)

coat1 = Coat(50)
costume1 = Costume(160)
costume2 = Costume(210)

total_cloth_consumption = 0
for wear in Clothes.instances:
    total_cloth_consumption += wear.cloth_consumption
print(f'Общий расход ткани: {total_cloth_consumption}')
coat.__del__()

total_cloth_consumption = 0
for wear in Clothes.instances:
    total_cloth_consumption += wear.cloth_consumption
print(f'Общий расход ткани: {total_cloth_consumption}')




