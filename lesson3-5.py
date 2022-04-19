#5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
#Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
def sum_num():
    s = 0 #s-переменна в которую будем складывать и выводить сумма, изначально она =0
    while True: #бесконечный цикл пишем так чтобы пользователь сам завершил работу
        in_list = input('Enter a number, input "q" to exit: ').split() #in_list- переменная, split раббивает черз пробел список слов в веденом предложении(цифры и/или буквы)
        for num in in_list: #  в цикле for: перебираем переменную num в списке-in_list
            if num.lower() == "q": # если введено q в нижнем регистре, то выходим
                return s # возвращаем cумму
            else:
                try:
                    s += int(num) #каждый введеный символ преобразуем в число
                except ValueError:#при сложении разных типов данных возникает ошибка
                    print("To exit the program, enter - 'q'.")#сообщаем пользователю о неккоректно введеных данных, поэтому можем суммировать числа после введеных букв, буквы идут в исключение
        print(f"Sum of numbers = {s}")
print(sum_num())