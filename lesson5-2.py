#2. Создать текстовый файл (не программно), сохранить в
# нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
with open("text_4.txt", "r", encoding='utf-8') as f_obj:#нет такого файла, возможно файл называется text_4.txt
    useful = [f'{line}. {count.strip()} - {len(count.split())} слов'#strip убирает все ненужные пробелы в строке
              #len-бурем строку и разбиваем ее на элементы и считаем их количество
              for line, count in enumerate(f_obj, 1)]#начинаем с индекса 1
    print(*useful, f"Всего строк -{len(useful)}.", sep="\n")
#*-распаковываем список и всесто одного списка принт видит 4 строки, которые должны чем то разделяться \n-каждый элемент с новой строки

print('*'*100)

with open("text_4.txt", encoding='utf-8') as f:
    my_line = f.readlines()
    for index, value in enumerate(my_line, 1):
        number_of_words = len(value.split())
        print(f'Строка {index} содержит {number_of_words} слов')

