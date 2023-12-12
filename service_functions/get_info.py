from seminar08_homework.custom_classes.exception_classes import LenNumberError, LenNameError


def check_criteria(data, criteria):
    if criteria == "имя" or criteria == "фамилию":
        return len(data) < 2
    elif criteria == "номер телефона":
        return len(str(data)) != 11


def get_valid_data(msg: str, exception_type: Exception) -> str:
    while True:
        try:
            data = input("Введите " + msg + ": ")
            if check_criteria(data, msg):
                raise exception_type
            else:
                return data
        except exception_type.__class__ as err:
            print(err)
            continue


def get_info() -> list:
    first_name = get_valid_data("имя", LenNameError("Имя слишком короткое"))
    last_name = get_valid_data("фамилию", LenNameError("Фамилия слишком короткая"))
    phone_number = get_valid_data("номер телефона", LenNumberError("Неверная длина номера телефона"))

    return [first_name, last_name, phone_number]
