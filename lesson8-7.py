# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу
# проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение
# созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber: #класс
    def __init__(self, real, imaginary): ##init-конструктор-спец метод при создании экземпляра класса, self- ссылка на объект
        self.real = real #аттрибут реальный
        self.img = imaginary #аттрибут воображаемый

    def __str__(self): #__str__() — срабатывает при передаче объекта функциям str() и print(), преобразует объект к строке,
        return f'{self.real}+{self.img}i' if self.img > 0 else f'{self.real}{self.img}i'

    def __add__(self, other): #__add__() — срабатывает при участии объекта в операции сложения в качестве операнда с левой стороны, обеспечивает перегрузку оператора сложения,
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __mul__(self, other): #__mul__(self, other) - умножение (x * y).
        return ComplexNumber((self.real * other.real - self.img * other.img),
                             (self.img * other.real + self.real * other.img))


cn = ComplexNumber(1, -2) #объект
cn1 = ComplexNumber(3, 4) #объект1
print(cn + cn1)
print(cn * cn1)
print(complex(1, -2) * complex(3, 4))  # calculation check
