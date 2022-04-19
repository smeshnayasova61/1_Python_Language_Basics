#6. Реализовать функцию int_func(), принимающую слова
# из маленьких латинских букв и возвращающую их же, но с
# прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
def int_func():
    for word in input('Введите слова через пробел(маленькими латинскими буквами):\n').split(): #'Enter words with a space(lower latin script):\n' и ищем переменную word в введенных пользователем словах
        chars = 0 # переменная, которая обнуляется, для каждого введенного пользователем слова она д.б. в нолевом состоянии
        for char in word: # ищем переменную char в переменной word
            if 97 <= ord(char) <=122:
                chars +=1
        print(word.title() if chars == len(word) else f"{word} - only small English letters!")
int_func()
