#2. Реализовать класс Road (дорога).
#определить атрибуты: length (длина), width (ширина);
#значения атрибутов должны передаваться при создании экземпляра класса;
#атрибуты сделать защищёнными;
#определить метод расчёта массы асфальта, необходимого для покрытия
# всей дороги;
#использовать формулу: длина*ширина*масса асфальта для покрытия
# одного кв. метра дороги асфальтом, толщиной в 1 см*число см
# толщины полотна;
#проверить работу метода.
#Например: 20 м*5000 м*25 кг*5 см = 12500 т.
class Road:
    def __init__(self, lenght, width): #__init__конструктор
        self._length = lenght #атрибут объекта длина дорожного полотна
        self._width = width #атрибут объекта ширина дорожного полотна

    def get_full_profit(self, weight=25, thickness=5): #get_full_profit метод
        return f"{self._length} м * {self._width} м * {weight} кг * {thickness} см =" \
               f"{(self._length * self._width * weight * thickness) / 1000} т" #формула толщины дорожного полотна

road_1 = Road(5000, 20)
print(road_1.get_full_profit())

print('*' * 100)

class Road:
    def __init__(self, le, wi):
        self._lenght = le
        self._width = wi

    def calc(self, weight=25, thickness=5):
        print(f"Масса асфальта - {self._lenght * self._width * weight * thickness / 1000} тонн")

    def main():
        while True:
            try:
                road_1 = Road(int(input('Введите ширину дороги в м: ')), int(input('Введите длину дороги в м: ')))
                road_1.calc()
                break
            except ValueError:
                print("Только целые числа!")
