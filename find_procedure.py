
# заготовка для домашней работы
# прочитайте про glob.glob
# https://docs.python.org/3/library/glob.html

# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции
# на зачёт с отличием, использовать папку 'Advanced Migrations'

import glob
import os.path
# просто для разминки... сужаем поиск изменяя параметр
#def find_file():
#   migrations = 'Migrations'
#    search_list = []
#    temp = ''
#    while True:
#        find_file = input('Введите строку:')
#        l = lambda x, y: x + '*' + y  
#        
#        param = '{}*.sql'.format(l(temp, find_file))
#        temp = l(temp, find_file)
#        print(param)
#        files = glob.glob(os.path.join(migrations, param))
#        for file in files:
#           print(file)
#        print(len(files))
#
#find_file()

def read_file():
    migrations = 'Migrations'
    files = glob.glob(os.path.join(migrations, "*.sql"))
    return files 

def iter(files, find_file):
    temp_list = []
    for item in files:
        if find_file in item:
             temp_list.append(item)
    return temp_list

def search_file(): 
    files = read_file()
    while True:
        find_file = input('Введите строку:')
        files = iter(files, find_file)
        for item in files:
            print(item)
        print('Всего: {}'.format(len(files)))

search_file()           

