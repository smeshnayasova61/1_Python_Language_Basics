# 1. Реализовать класс Matrix (матрица). Обеспечить
# перегрузку конструктора класса (метод __init__()), который
# должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода
# матрицы в привычном виде. Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух
# матриц). Результатом сложения должна быть новая матрица. Подсказка:
# сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
#a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
# b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]

# class Matrix:
#     def __init__(self, lists):
#         self.lists = lists

    # def __str__(self): #str отвечает за перегрузку конструктора класса init
    #     return '\n'.join(map(str, self.lists))
    #
    # def __add__(self, other): #отвечает за сумму
    #     c = [] # подготавливаем пустой список-будет матрица, кот мы вернем
    #     for i in range(len(self.lists)): # работаем в диапазоне длины 1 матрицы
    #     # цикл перебирает внешний список
    #         c.append([])# добавление еще одного подсписка
    #         for j in range(len(self.lists[0])):
    #         #цикл перебирает внутренние списки
    #             c[i].append(self.lists[i][j] + other.lists[i][j])
    #              # в список добавили подсписок под индексом 0 и наполняем его суммами элементов
    #              # 5, 1. 3, 1, 1, 1, 6, 2 итд - и суммируем их
    #         return '\n'.join(map(str, c))
    #         #возвращаем объект данного класса, чтобы выполнить дальнейшее суммирование

# matrix_1 = Matrix(a)
# matrix_2 = Matrix(b)
# print(f"Matrix 1\n{matrix_1}\n{'-' * 20}")
# print(f"Matrix 2\n{matrix_2}\n{'-' * 20}")
# print(f"matrix 1 + matrix 2\n{matrix_1 + matrix_2}")

print('*'*100)

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join('\t'.join([f"{itm:03}" for itm in line]) for line in self.data)
        #список преобразуем к строке, \t-табуляция, объедин все элементы списка, убирает все скобки и зпт,
        # \n объедин всю конструкцию
    def __add__(self, other):
        try:
            m =[[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
                for line in range(len(self.data))]
            #элементы этого списка будут подсписки
            return Matrix(m)
        #возвращаем объект
        except IndexError:
            return f'Ошибка размерностей матриц'


m_1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_2 = [['5', '7', '23'], ['9', '23', '-54'], ['12', '3', '16']]
mtrx_1  = Matrix(m_1)
mtrx_2 = Matrix(m_2)
new_m = mtrx_1 + mtrx_2

# stroki = int(input("Введите количество строк и столбцов матрицы: "))
# stolbcy = stroki
#
# matrix1 = Matrix([[i * j for j in range(stroki)] for i in range(stolbcy)])
# matrix2 = Matrix([[i + j for j in range(stroki)] for i in range(stolbcy)])
#
# print('First matrix:\n', matrix1, end='\n\n')
# print('Second matrix:\n', matrix2, end='\n\n')
# print('Summ of first and second matrix:\n', matrix1 + matrix2)

print('*'*100)

from itertools import  zip_longest # в модуле itertools находится функция zip_longest(если элемент
# нельзя ни с чем застрегнуть она добавляем None-для разноразмерных матриц)

class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self): #str-перегрузка
        return  str('\n'.join(['\t'.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other): #не добавляем переменную, а возвращаем объект
        return Matrix([map(sum, zip_longest(*t, fillvalue=0))
                       for t in zip_longest(self.matrix, other.matrix, fillvalue=[])]) # след действ: производим сумму использую Map, использ оператор распаковки zip_longest, 3 индекс в матрице n заполняем fillvalue=[], без пустоко списка будет сумма 3 индекса и None-ошибка
                        #объедин матрицу m и n, матрицы разноразмерные поэтому 3 элемент матрицы m, вместо None нужно заполнить пустым списком- fillvalue=[]

m = [[1, 2, 3], [3, 4, 5], [1, 2]]
n = [[9, 8, 7], [7, 6, 5]]

matr_1 = Matrix(m)
matr_2 = Matrix(n)

print(matr_1)
print(matr_1 + matr_2)

print('*'*100)

class Matrix:
     def __init__(self, matrix):
         self.matrix = matrix

     def __str__(self): #перегрузка
         return '\n'.join(map(lambda r: ' '.join(map(str, r)), self.matrix)) + '\n'

     def __add__(self, other): #add перегружен с использованием функций lambda
         return Matrix(map(lambda r_1, r_2: map(lambda x, y: x + y, r_1, r_2), self.matrix, other.matrix))
         # map берет по одному элементу из итерабельного объекта, в данном случае берем 2 элемента и предоставляем 2 итерабельных объекта
         # в r_1 список  под индексом 0 переменной my_m1,  а r_2 - my_m2, потом lanbda произведет обмен значениями и получим сумму

     my_m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
     my_m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
     print(my_m1)
     print(my_m2)
     s = my_m1 + my_m2
     print(s)




