# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые 
# должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)e
# 4. Использование функций. Ваша программа не должна быть линейной

from service_functions.main import main

main('phone.csv')

# Дополнить справочник возможностью
# копирования данных из одного файла в другой.
# Пользователь вводит номер строки, которую
# необходимо перенести из одного файла в другой.