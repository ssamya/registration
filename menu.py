import main
import os


def main_menu():
    while True:
        person_input = int(input("1) Registration\n2) Authorization\n"))
        if person_input != 1 and person_input != 2:
            print("\nPlease choose from the list:\n")
            main_menu()
        elif person_input == 1:
            if not os.path.isfile("test.csv"):
                main.add_writeheader()
                valid(main.add_to_csv(registration()))
            else:
                valid(main.add_to_csv(registration()))
        elif person_input == 2:
            check(main.logining(authorization()))


def registration():
    log = str(input("Enter your username: \n"))
    mail = str(input("Enter your email: \n"))
    password = str(input("Enter your password: \n"))
    add_dict = {"login": log, "email": mail, "password": password}
    return add_dict


def authorization():
    alog = str(input("Enter username: \n"))
    apass = str(input("Enter password: \n"))
    authorization_dict = {"login": alog, "password": apass}
    return authorization_dict


def check(response: bool):
    if response:
        print("Successful login!")
    else:
        print("The data was not found")


def valid(value: bool):
    if not value:
        print("The password must contain more 8 symbols.\nPlease, try again.")
    else:
        print("Successful registration!")

