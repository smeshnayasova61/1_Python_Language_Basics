# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные
# типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, общие для
# приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа
# оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают
# за приём оргтехники на склад и передачу в определённое подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
# любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на склад, нельзя
# использовать строковый тип данных. Подсказка: постарайтесь реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.

class OfficeEquipment:
    ''' Оргтехника '''

    def __init__(self, model, price, dpi, paper_size):
        self._model = model
        self._price = price
        self._dpi = dpi
        self._paper_size = paper_size

    @property
    def model(self):
        return self._model


class Printer(OfficeEquipment):
    ''' Принтер '''

    def __init__(self, model, price, dpi, paper_size, jet_type):
        self.jet_type = jet_type
        super().__init__(model, price, dpi, paper_size)


class Scanner(OfficeEquipment):
    ''' Сканер '''


class Copier(OfficeEquipment):
    ''' Копир '''

    def __init__(self, model, price, dpi, paper_size, print_speed, monthly_print_volume):
        self.print_speed = print_speed
        self.monthly_print_volume = monthly_print_volume
        super().__init__(model, price, dpi, paper_size)


class Warehouse:
    ''' Склад '''
    __equipments = dict()
    __issued_equipments = dict()

    def add_Equipment(self, key, value):
        ''' Приём оргтехники на склад '''
        if self.__equipments.get(key) == None:
            self.__equipments[key] = 0
        self.__equipments[key] += value

    def issue_Equipment(self, key, value):
        ''' Выдача оргтехники со склада '''
        rest = self.__equipments.get(key)
        if rest != None and rest >= value:
            self.__equipments[key] -= value
            if self.__equipments[key] == 0:
                del self.__equipments[key]

    def num(self, key):
        value = self.__equipments.get(key)
        return value if value != None else 0

    def equipments_in_warehouse(self):
        print('\n------------------------------------\nЗапасы на складе:\n------------------------------------')
        for i in self.__equipments:
            print(f'{models[i].model} - {self.num(i)} шт.')
        print('------------------------------------')

    def issued_equipments(self):
        ''' Вывод информации овыданной оргтехикие '''
        print(f'\nIssued to office:\n{self.__equipments}')


# список моделей оргтехники
models = [Printer('HP Laserjet 2130', 1950, '4800x1200', 'A4', 'laserjet'),
          Printer('CANON Pixma MG3640S BK', 3640, '4800x1200', 'A4', 'inkjet'),
          Copier('XEROX CopyCentre C118', 87800, '600x600', 'A3', 18, 10000),
          Scanner('EPSON Perfection V19', 5110, '4800×4800', 'A3')]

warehouse = Warehouse()
warehouse.equipments_in_warehouse()

while True:
    # меню операций
    print('\nВведите тип операции:\n<1> Принять на склад.\n<2> Выдать со склада.\n<Enter> Выход.')
    action = input(' > ')
    if action in ['1', '2']:  # если выбрана операция
        # формируем список оргтехники
        s = ''
        for i, eq in enumerate(models):
            s += f'\n<{i}> {eq.model} ({warehouse.num(i)} шт.)'
        # меню оргтехники
        while True:
            print(f'\nВведите модель оргтехники и кол-во:{s}')
            # выбираем модель
            try:
                model = int(input('модель > '))
                if model in range(len(models)):
                    # вводим кол-во
                    n = int(input('кол-во > '))
                    if (n <= 0):
                        raise ValueError
                else:
                    raise ValueError

            except ValueError:
                print(f'Некорректный ввод. Введите число от <0> до <{len(models)}>.')
                continue
            else:
                # совершаем операцию
                print('\nОперация:')
                if (action == '1'):  # принимаем технику на склад
                    print(f'Принято на склад {models[model].model} - {n} шт.')
                    warehouse.add_Equipment(model, n)
                elif (action == '2'):  # выдаём технику со склада
                    max = warehouse.num(model)
                    if (n > max):  # если запрошено больше, чем есть
                        n = max
                        print(f'Внимание: На складе всего {n} шт. {models[model].model}!')
                    print(f'Выдано со склада {models[model].model} - {n} шт.')
                    warehouse.issue_Equipment(model, n)

                # выводим остатки по складу
                warehouse.equipments_in_warehouse()
                break

            if (input('\nPress <Enter> to continue or any key to exit...') != ''):
                break
    elif action == '':  # если выбран выход - завершаем работу
        break
    else:
        print('Некорректный ввод. Для выбора введите <1> или <2>.')

#  ------------------------------------------- вариант решения ---------------------------------------------------------
import datetime
from abc import ABC, abstractmethod
from view import Show_dict_cards, Show_dict_storage_points, Show_balans_storage_point


class Essence:
    def __init__(self, name):
        self._name = name
        self._id = None

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name


class Dict_entities(dict):
    def __init__(self, name):
        super().__init__()
        self._name = name
        self._id_counter = 0

    def add(self, essence):
        essence.set_id(self._id_counter)
        self[self._id_counter] = essence
        self._id_counter += 1
        return essence.get_id()

    def get_name(self):
        return self._name


class Dict_cards(Dict_entities):
    def __init__(self):
        super().__init__('Список карточек ТМЦ')


class Card_item(Essence):
    def __init__(self, name, description='', price=0.0):
        super().__init__(name)
        # description - описание ТМЦ
        # price - цена за единицу
        self._description = description
        self._price = price

    def get_description(self):
        return self._description

    def get_price(self):
        return self._price


class Dict_storage_points(Dict_entities):
    # Словарь точек хранения
    def __init__(self):
        super().__init__('Список точек хранения и контрагентов.')


class Dict_move_item(Dict_entities):
    # Словарь записей в амбарную книгу
    def __init__(self, name):
        super().__init__(name)


class Record_move_item(Essence):
    # Запись в амбарную книгу о перемещении ТМЦ
    def __init__(self, dttm, st_pnt, move_st_pnt, card, quantity):
        super().__init__('')
        # _dttm - дата и время двиения ТМЦ
        # _st_pnt -  точка хранения
        # _move_st_pnt - корреспондирующая точка хранения. Если приход то откуда, если расход то куда
        # _произоло перемещение ТМЦ
        # _card - карточки ТМЦ
        # _quantity - количество перемещаемых едениц ТМЦ если положительное то приход, если отрицательное то расход
        self._dttm = dttm
        self._st_pnt = st_pnt
        self._move_st_pnt = move_st_pnt
        self._card = card
        self._quantity = quantity

    def get_dttm(self):
        return self._dttm

    def get_card(self):
        return self._card

    def get_quantity(self):
        return self._quantity


class Movable_item:
    def __init__(self, st_pnt, card, quantity):
        self._st_pnt = st_pnt
        self._card = card
        self._quantity = quantity

    def get_st_pnt(self):
        return self._st_pnt

    def get_card(self):
        return self._card

    def get_quantity(self):
        return self._quantity


class Storage_point(Essence):
    def __init__(self, name, description, provider, dict_move_item, dict_cards):
        super().__init__(name)
        self._description = description
        self._provider = provider  # True - организация поставщик, False - точка хранения
        self._dict_move_item = dict_move_item
        self._dict_cards = dict_cards
        self._list_id_move_items = []

    def get_description(self):
        return self._description

    def get_provider(self):
        return self._provider

    def income(self, movable_item):
        record_move_item = Record_move_item(datetime.datetime.now(), self, movable_item.get_st_pnt(),
                                            movable_item.get_card(), movable_item.get_quantity())

        self._list_id_move_items.append(self._dict_move_item.add(record_move_item))
        # self._dict_move_items.add
        #
        #
        #
        pass

    def flow(self, new_st_pnt, card, quantity):
        if self.calc_balance(card) >= quantity:
            record_move_item = Record_move_item(datetime.datetime.now(), self, new_st_pnt, card, -quantity)

            #      добавляю запись о расходе
            self._list_id_move_items.append(self._dict_move_item.add(record_move_item))
            #      формирую movable_item
            movable_item = Movable_item(self, card, quantity)

            #      Передаю Inventory_item на новую точку хранения
            new_st_pnt.income(movable_item)
        # else:
        #     # возвращаю отказ в перемещении
        #     pass
        pass

    def calc_balance(self, card):
        # расчитывается остаток ТМЦ карточке
        balance = 0
        for i in self._list_id_move_items:
            if self._dict_move_item[i].get_card() is card:
                balance += self._dict_move_item[i].get_quantity()
        return balance

    def get_list_cards(self):
        # Возвращает список карточек ТМЦ, по которым было дижение на данной точке хранения
        list_id_cards = []
        list_card = []
        for i in self._list_id_move_items:
            list_id_cards.append(self._dict_move_item[i].get_card().get_id())
        for i in frozenset(list_id_cards):
            list_card.append(self._dict_cards[i])
        return list_card


def main():
    dict_move_item = Dict_move_item('')

    dict_cards = Dict_cards()
    dict_cards.add(Card_item('Компьютер', 'DeskTop', 25000.0))
    dict_cards.add(Card_item('Компьютер', 'Notebook', 35000.0))
    dict_cards.add(Card_item('Принтер', 'HP Laser Jet 1018', 6000.0))
    dict_cards.add(Card_item('Картридж', 'HP Q2612L экономичный 12L', 780.0))

    print()
    Show_dict_cards(dict_cards)()

    dict_storage_points = Dict_storage_points()
    dict_storage_points.add(Storage_point('Поставщик', 'Oldi', True, dict_move_item, dict_cards))
    dict_storage_points.add(Storage_point('Поставщик', 'ФЦентр', True, dict_move_item, dict_cards))
    dict_storage_points.add(Storage_point('Склад', 'Г-образная комната', False, dict_move_item, dict_cards))
    dict_storage_points.add(
        Storage_point('Склад', 'Помещение кроссового оборудования', False, dict_move_item, dict_cards))
    dict_storage_points.add(Storage_point('Цех №3', 'ТМЦ переданные в производство', False, dict_move_item, dict_cards))
    dict_storage_points.add(Storage_point('Списание', 'ТМЦ списанные ', False, dict_move_item, dict_cards))
    dict_storage_points.add(
        Storage_point('Утилизация', 'ООО \"Инвестиции в будущее\"', True, dict_move_item, dict_cards))

    print()
    Show_dict_storage_points(dict_storage_points)()

    Show_balans_storage_point(dict_storage_points[0])()
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[0], 5))
    Show_balans_storage_point(dict_storage_points[0])()

    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[1], 5))
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[2], 5))
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[3], 5))

    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[0], 5))
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[1], 5))
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[2], 5))
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[3], 5))

    dict_storage_points[1].income(Movable_item(dict_storage_points[1], dict_cards[3], 6))
    dict_storage_points[1].income(Movable_item(dict_storage_points[1], dict_cards[3], 12))
    dict_storage_points[0].income(Movable_item(dict_storage_points[0], dict_cards[2], 5))

    dict_storage_points[1].flow(dict_storage_points[2], dict_cards[3], 12)
    dict_storage_points[0].flow(dict_storage_points[3], dict_cards[0], 3)

    print()
    Show_balans_storage_point(dict_storage_points[0])()
    Show_balans_storage_point(dict_storage_points[1])()
    Show_balans_storage_point(dict_storage_points[2])()
    Show_balans_storage_point(dict_storage_points[3])()
    Show_balans_storage_point(dict_storage_points[4])()


if __name__ == '__main__':
    main()

#  -------------------------------------------------------- модуль view ------------------------------------------------

import datetime


class Show_dict_cards:
    def __init__(self, dict_cards):
        self._dict_cards = dict_cards

    def __call__(self):
        print(f'  {self._dict_cards.get_name()}')
        print('+--------------+-----------------+---------------------------------------------+--------------+')
        print('|           id | Категория ТМЦ   | Описание                                    |  Цена за ед. |')
        print('+--------------+-----------------+---------------------------------------------+--------------+')
        for key, card_item in self._dict_cards.items():
            print(
                f'| {card_item.get_id():12} | {card_item.get_name():15} | {card_item.get_description():43} | {card_item.get_price():12.2f} |')
        print('+--------------+-----------------+---------------------------------------------+--------------+')


class Show_dict_storage_points:
    def __init__(self, dict_storage_points):
        self._dict_storage_points = dict_storage_points

    def __call__(self):
        print(f'  {self._dict_storage_points.get_name()}')
        print('+--------------+-----------------+---------------------------------------+-----+')
        print('|           id | Наименование    | Описаниея                             |Контр|')
        print('+--------------+-----------------+---------------------------------------+-----+')

        for key, storage_point in self._dict_storage_points.items():
            sprovider = 'Да' if storage_point.get_provider() else 'Нет'
            print(
                f'| {storage_point.get_id():12} | {storage_point.get_name():15} | {storage_point.get_description():37} | {sprovider:3} |')

        print('+--------------+-----------------+---------------------------------------+-----+')


class Show_balans_storage_point:
    def __init__(self, storage_point):
        self._storage_point = storage_point

    def __call__(self):
        print()
        print(
            f'Остатки на точке хранения: {self._storage_point.get_name()} ({self._storage_point.get_description()}) (id = {self._storage_point.get_id()})')
        print(f'по состоянию на {datetime.datetime.now()}')
        if len(self._storage_point.get_list_cards()) > 0:
            _total = 0.0
            print(
                '+--------------+-----------------+---------------------------------------------+--------------+-------------+--------------+')
            print(
                '|           id | Категория ТМЦ   | Описание                                    |  Цена за ед. |     Остаток |        Сумма |')
            print(
                '+--------------+-----------------+---------------------------------------------+--------------+-------------+--------------+')

            for i in self._storage_point.get_list_cards():
                _sum = i.get_price() * self._storage_point.calc_balance(i)
                _total += _sum
                print(
                    f'| {i.get_id():12} | {i.get_name():15} | {i.get_description():43} | {i.get_price():12.2f} |{self._storage_point.calc_balance(i):12} | {_sum:12.2f} |')
            print(
                '+--------------+-----------------+---------------------------------------------+--------------+-------------+--------------+')
            print(
                f'                                                                                                      Итого:  {_total:12.2f} ')
        else:
            print('Остатки не выявлены')