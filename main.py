import csv
import re
import errors


def csv_reader():
    with open("test.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        result = list(reader)
        return result


def check_email(mail):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, mail):
        return True
    else:
        return False


def add_to_csv(some_dict: dict):
    user_dict = some_dict.copy()
    if not user_dict["login"]:
        raise errors.EmptyLoginError
    elif not user_dict["password"]:
        raise errors.EmptyPasswordError
    elif not user_dict["email"]:
        raise errors.EmptyEmailError
    elif len(user_dict["password"]) < 8:
        return False
    else:
        if check_email(user_dict["email"]):
            with open("test.csv", "a", encoding="utf-8", newline="") as csv_file:
                fieldnames = ["login", "email", "password"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow(user_dict)
                return True
        else:
            raise errors.InvalidEmailError


def logining(some_dict: dict):
    dict_list = csv_reader()
    for row in dict_list:
        if some_dict["login"] == row["login"] and some_dict["password"] == row["password"]:
            return True

    return False


def add_writeheader():
    with open("test.csv", "w", encoding="utf-8", newline="") as csv_file:
        fieldnames = ["login", "email", "password"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

