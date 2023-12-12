from os.path import exists
from seminar08_homework.service_functions.get_info import get_info
from seminar08_homework.service_functions.file_operations import create_file, read_file, write_file, search_in_file, \
    copy_file


def main(file_name):
    while True:
        print("Доступные команды: q - выход, w - запись, r - чтение, s - поиск, c - копирование")
        command = input("Введите команду: ")
        match (command):
            case "q":
                break

            case "w":
                if not exists(file_name):
                    create_file(file_name)
                write_file(file_name, get_info())
                
            case "r":
                if not exists(file_name):
                    print("Файл отсутствует. Создайте его")
                    continue
                output = read_file(file_name)
                for i in range(len(output)):
                    print(output[i])
            
            case "s":
                if not exists(file_name):
                    print("Файл отсутствует. Создайте его")
                    continue
                output = search_in_file(file_name)
                for i in range(len(output)):
                    print(output[i])

            case "c":
                if not exists(file_name):
                    print("Файл отсутствует. Создайте его")
                    continue
                copy_file(file_name)