import getpass

from input import checker


def request_emails(send_mail, number_mails):
    mails = []
    if send_mail:
        for i in range(number_mails):
            valid = False
            num = 0
            while not valid:
                try:
                    mail = input(f"Person {i + 1} write your e-mail: ")
                    checker.check_mail(mail)
                    valid = True
                    mails.append(mail)
                except Exception as e:
                    print(e)
    return mails


def request_file_secret():
    file = ""
    valid = False
    while not valid:
        try:
            file = input(f"Write the file that contains the sharing secret: ")
            checker.check_file(file)
            valid = True
        except Exception as e:
            print(e)
    return file


def request_integer():
    valid = False
    num = 0
    while not valid:
        try:
            num = int(input("Enter a number: "))
            valid = True
        except ValueError:
            print('Error, insert a number')

    return num


def request_secret_terminal():
    valid = False
    secret = ""
    while not valid:
        try:
            secret = getpass.getpass("Enter the sharing secret you want to encrypt:")
            checker.check_secret(secret)
            valid = True
        except Exception as e:
            print(e)
    return secret


def request_amount_people():
    amount = 0
    print("Enter the amount of people.")
    while True:
        try:
            amount = request_integer()
            checker.check_amount_people(amount)
        except Exception as e:
            print(e)
        else:
            break
    return amount


def request_minimum_to_recover(m):
    number = 0
    print("Enter the minimum number of people to retrieve the sharing secret.")
    while True:
        try:
            number = request_integer()
            checker.check_minimum_people(m, number)
        except Exception as e:
            print(e)
        else:
            break
    return number


def request_keys(number_keys):
    keys = []
    i = 0
    while i < number_keys:
        try:
            key = getpass.getpass(f'Person {i + 1}:Enter your private key:')
            checker.check_key(key)
            keys.append(key)
            i += 1
        except Exception as e:
            print(e)
    return keys
