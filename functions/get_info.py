from classes.exception_classes import LenNumberError, LenNameError


def check_criteria(data, criteria):
    if (criteria == "имя" or criteria == "фамилию"):
        return len(data) < 2
    elif (criteria == "номер телефона"):
        return len(str(data)) != 11

def get_valid_data(msg : str, exception_type : Exception) -> str:
    is_valid_data = False
    while not is_valid_data:
        try:
            data = input("Введите " + msg + ": ")
            if check_criteria(data, msg):
                raise exception_type
            else:
                is_valid_data = True
        except exception_type.__class__ as err:
            print(err)
            continue
    return data

def get_info() -> list:
    first_name = get_valid_data("имя", NameError("Введено некорректное значение"))
    last_name  = get_valid_data("фамилию", NameError("Введено некорректное значение"))
    phone_number  = get_valid_data("номер телефона", LenNumberError("Неверная длина номера телефона"))

    return [first_name, last_name, phone_number]