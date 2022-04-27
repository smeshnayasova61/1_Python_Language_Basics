#3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не
# менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт
# средней величины дохода сотрудников.
#Пример файла:
#Иванов 23543.12
#Петров 13749.32
with open('text_3.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for  line in f}
    #словарь: 0 -фамилия, 1 -зп-индексы в списке f, собираем словарь ключ-фамилия: значение-зп
    print(f'Average salary = {round(sum(employees_dict.values())/ len(employees_dict), 3)}\n'
          f'Employees with salary less than 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')

print('*' * 100)

def task_3():# нет файла task_3.txt
    wages = {}
    try:
        with open('task_3.txt', 'r', encoding='utf-8') as file:
            for line in file:
                wages[line.split()[0]] = float(line.split()[1])
        print('Меньше 20000 получают: ')
        for name, wage in wages.items():
            if wage < 20000:
                print(name)
        print(f'Средняя зарплата равна {sum(wages.values()) / len(wages)}')
    except IOError:
        print('Бухгалтер сбежал с ведомостью. Зарплаты не будет')
    except:
        print('Что-то пошло не так')

