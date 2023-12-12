from csv import DictReader, DictWriter
from seminar08_homework.service_functions.get_info import get_valid_data
from seminar08_homework.custom_classes.exception_classes import LenNumberError, LenNameError


def create_file(file_name):
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name, lst):
    res = read_file(file_name)
    for el in res:
        if el["Телефон"] == str(lst[2]):
            print("Такой телофон уже есть")
            return

    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)


def search_in_file(file_name):
    while True:
        print("----------------")
        print("Выберите критерий поиска:")
        print("1 - по имени")
        print("2 - по фамилии")
        print("3 - по номеру телефона")
        criteria = input("Критерий поиска: ")
        print("----------------")
        match criteria:
            case "1":
                field_name = "Имя"
                searching_item = get_valid_data("имя", LenNameError("Имя слишком короткое"))
                break
            case "2":
                field_name = "Фамилия"
                searching_item = get_valid_data("фамилию", LenNameError("Фамилия слишком короткая"))
                break
            case "3":
                field_name = "Телефон"
                searching_item = get_valid_data("номер телефона", LenNumberError("Неверная длина номера телефона"))
                break
            case _:
                print("Выбран неверный критерий")

    data_dictionary = read_file(file_name)

    res_list = list()

# поиск всех вхождений искомого значения
#  (например, несколько записей с одинаковыми именами)
    for el in data_dictionary:
        for key, value in el.items():
            if key == field_name and value == searching_item:
                res_list.append(el)
    return res_list


def copy_file(file_name):
    new_file_name = input("Введите имя файла принимающего строку: ")
    while True:
        try:
            line_number = int(input("Введите номер строки: "))
            break
        except Exception:
            print("Введен неверный номер строки")

    with open(file_name, "r", encoding='utf-8') as data:
        for _ in range(line_number):
            f_reader = DictReader(data)

    with open(new_file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writerows(f_reader)