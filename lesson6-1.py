#1. Создать класс TrafficLight (светофор).
#определить у него один атрибут color (цвет) и метод running (запуск);
#атрибут реализовать как приватный;
#в рамках метода реализовать переключение светофора в режимы: красный,
# жёлтый, зелёный;
#продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#переключение между режимами должно осуществляться только в
# указанном порядке (красный, жёлтый, зелёный);
#проверить работу примера, создав экземпляр и вызвав описанный метод.
#Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать
# скрипт.

from time import sleep
class TrafficLight:
    __color = "Темно-синий"#атрибут класса приватный
    def running(self):#метод класса
        while True:
            print("Trafficlight is red now")
            sleep(7)
            print("Trafficlight is yellow now")
            sleep(2)
            print("Trafficlight is green now")
            sleep(7)
            print("Trafficlight is yellow now")
            sleep(2)

trafficlight = TrafficLight()#объект класса
trafficlight.running()#запускаем светофор

print('*' * 100)

import time
import itertools

class TrafficLight:
    __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]]]#набор значений
    #список списков-подсписок-вводимый текст, тайминг и цвет

    def running(self):
        for light in itertools.cycle(self.__color):
            #сделали цикл бесконечным за счет модуля itertools в котором есть бесконечный итератор cycle с набором значений
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")#специальная формула
            #end-не позволяет курсору перейти на след стр, \r-возвращ курсор на начало стр
            time.sleep(light[1][0])

traffic_light_1 = TrafficLight()
traffic_light_1.running()

print('*' * 100)

import time
import itertools

class TrafficLight:
    __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]]]#набор значений
    #список списков-подсписок-вводимый текст, тайминг и цвет

    def __init__(self, light_list):
        self.light_list = light_list

    def running(self):
        if len([i for i in self.light_list if i in ["red", "yellow", "green"]]) >=3:
            for light in itertools.cycle(self.__color):
                print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
                time.sleep(light[1][0])
        else:
            print("Ваш список цветов неверен.")
trafic_light_1 = TrafficLight(["lilac", "green", "lime", "white", "black", "yellow"])
trafic_light_1.running()

print('*' * 100)

from time import sleep
from itertools import cycle

class TrafficLight:
    # __color = [['RED', 'YELLOW', 'GREEN'], [7, 2, 4],
    __color = [" ", [7, 2, 4], ["\033[41m\033[1m", "\033[43m\033[1m", "\033[42m\033[1m"]]
    #пустая строка с(), тайминги и цвета-атрибут класса

   def running(self):
        col_lst = ["", ""]
        for n in cycle((0, 1, 2)):
            col_lst[1] = self.__color[2][n]
            print(f"\r({col_lst[int(n==0)]}{self.__color[0]}\033[0m)"
                  f"({col_lst[int(n==1)]}{self.__color[0]}\033[0m)"
                  f"({col_lst[int(n==2)]}{self.__color[0]}\033[0m)", end='')
            sleep(self.__color[1][n])

tr_light = TrafficLight()
tr_light.running()

print('*' * 100)

from time import sleep
import colorama
import sys
colorama.init()

class TrafficLight:
     #Запуск в терминале
    def running(self):
        while True:
            print(f'\r\033[31m{chr(11035)} ', end='')
            sleep(4)
            print(f'\r\033[30m{chr(11035)} ')
            print(f'\r\033[33m{chr(11035)} ', end='')
            sleep(2)
            print(f'\r\033[30m{chr(11035)} ')
            print(f'\r\033[32m{chr(11035)} ', end='')
            sleep(4)
            print(f'\r\033[30m{chr(11035)} ', end='')
            sys.stdout.write('\r\x1b[2A')
            #с помощью модуля sys прийдется перепрыгнуть через строки

trafficLight = TrafficLight()
trafficLight.running()

print('*' * 100)

import tkinter as tk
from PIL import ImageTk, Image
from itertools import cycle

class TrafficLight:
    def __init__(self, working_algorithm):
        self.sec_count = 0
        self.working_algorithm = working_algorithm
        self.img_dict = {'red': Image.open('pic/red.jpg').resize((250, 350)),
                         'yellow': Image.open('pic/yellow.jpg').resize((250, 350)),
                         'green': Image.open('pic/green.jpg').resize((250, 350)),
                         'red+yellow': Image.open('pic/red_yellow.jpg').resize((250, 350)),
                         'off': Image.open('pic/off.jpg').resize((250, 350))}
        self.iterator = cycle(self.working_algorithm)
        self.cur_state = next(self.iterator)

        self.root = tk.Tk()
        self.root.attributes("-topmost", True)
        self.root.geometry('300*400')
        image = ImageTk.PhotoImage(self.img_dict[self.cur_state[0]])

    def running(self):
        self.sec_count += 1
        if self.sec_count == self.cur_state[1]:
            self.cur_state = next(self.iterator)
            self.sec_count = 0
            cur_img = ImageTk.PhotoImage(self.img_dict[self.cur_state[0]])
            self.label.configure(image=cur_img)
            self.lable.photo_ref = cur_img
            self.lable.pack()
        self.root.after(100, self.running)

mode = input("Enter traffic-light mode (0 - simple, 1-advaced):")
if mode == '0':
    app = TrafficLight([('red', 70), ('yellow', 20), ('green', 50), ('yellow', 20)])
elif mode == '1':
    app = TrafficLight([('red', 70),
                        ('red+yellow', 20),
                        ('green', 50),
                        ('off', 5),
                        ('green', 5),
                        ('off', 5),
                        ('green', 5),
                        ('off', 5),
                        ('green', 5),
                        ('yellow', 20)])
else:
    print('Wrong choice!')








