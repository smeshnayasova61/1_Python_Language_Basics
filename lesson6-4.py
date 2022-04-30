# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась,
# повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
# PoliceCar;
# добавьте в базовый класс метод show_speed, который должен
# показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
# выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы
# и покажите результат.

from random import choice

class Car:
    #main car
    direction = ["north", "northeast", "east", "southeast", "south",
                 "southwest", "west", "northwest"]

    def __init__(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p
        print(f'New car: {n} has a color: {c}.\nIs the car a police car? {p}')

    def go(self):
        print(f'{self.name}: Car went.')

    def stop(self):
        print(f'{self.name}: Car stopped!')

    def turn(self):
        print(f'{self.name}: Car turned {choice(self.direction)}.')

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}.'

class TownCar(Car):
    """City car"""

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 60 else super().show_speed()

class WorkCar(Car):
    """Cargo truck"""

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 40 else super().show_speed()

class SprotCar(Car):
    """Sports car"""

class PoliceCar(Car):
    """Patrol car"""

    def __init__(self, n, c, s):
        super().__init__(n, c, s, p=True)

police_car = PoliceCar('"Полицейская"', 'белый', 80)
work_car = WorkCar('"Грузовик"', 'хакки', 40)
sport_car = SprotCar('"Спортивная"', 'красный', 120)
town_car = TownCar('"Малютка"', 'желтый', 65)

list_of_cars = [police_car, work_car, sport_car, town_car]

for i in list_of_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()



