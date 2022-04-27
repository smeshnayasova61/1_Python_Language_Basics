# 4. Создать (не программно) текстовый файл со
# следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в
# новый текстовый файл.
rus_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open('text_4_4.txt', "w", encoding='utf-8') as new_file:#создать файл
    with open('text_4.txt', encoding='utf-8') as my_files:
        new_file.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0])) for line in my_files])

    print('*' * 100)
#pip install googletrans==4.0.0rc1
#обновление до альфа-версии
from googletrans import Translator
with open('text_4.txt_translate.txt', 'w', encoding='utf-8') as f:
    with open('text_4.txt', 'r', encoding='utf-8') as f1:
        text = f1.read()
    try:
        f.write(Translator().translate(text, dest = 'ru').text)
    except AttributeError:
        print("DDoS-така на Google не прошла, продолжай попытки!")

print('*' * 100)

#from textblob import TextBlob#не найдет модуль textblob
#with open('text_4.txt', 'r', encoding='utf-8') as en_f, \
#    open('text_4_4.txt', 'w', encoding='utf-8') as ru_f:
#    ru_f.write(str(TextBlob(en_f.read()).translate(to='ru')))

print('*' * 100)

import requests
import json
"""Переводит с английского на русский файл, результат записывается в новый файл.
Должен быть установлен модуль requests"""
token = "trnsl.1.1.20200416T1325512Z.0bdb58c00f70557b.b1aec4edc72e76cc6c08980f7ed0c2de92ae86"
url_trans = 'https://translate.yandex.net/api/v1.5/tr/json/translate'
with open('task_4.txt', encoding='utf-8') as f_result:#нет такого файла в директории
    with open('text_4.txt', encoding='utf-8') as f_4:
        for line in f_4:
            eng_text = line
            trans_option = {'key': token, 'lang': 'en-ru', 'text': eng_text}
            webRequest = requests.get(url_trans,params=trans_option)
            trans_dict = json.loads(webRequest.text)
            line_to_result = "".join(trans_dict["text"])
            f_result.write(line_to_result)
    print(f'Text translate from {f_4.name} has been done in {f_result.name}')
