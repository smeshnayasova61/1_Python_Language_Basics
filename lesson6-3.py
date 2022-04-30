# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income
# (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage,
# "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учётом премии
# (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры
# класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров.

class Worker: #родитель
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"Profit": wage, "bonus": bonus} #защищенный атрибут
        #класса, ссылается на словарь, словарь собираем в конструкторе

class Position(Worker): #класс должность на базе класса работние, класс потомок
    def get_full_name(self): #метод класса
        return f"{self.name} {self.surname}"

    def get_total_income(self): #метод класса
        return sum(self._income.values()) #сумма значений словаря income

manager = Position("Dorian", "Grey", "CEO", 500000, 125000)
print(manager.get_full_name())
print(manager.position)
print(manager.get_total_income())

