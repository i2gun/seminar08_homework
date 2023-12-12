from os.path import exists
from functions.get_info import get_info
from functions.file_operations import create_file, read_file, write_file, search_in_file


def main(file_name):
    while True:
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
                print(*read_file(file_name))
            
            case "s":
                if not exists(file_name):
                    print("Файл отсутствует. Создайте его")
                    continue
                print(*search_in_file(file_name))