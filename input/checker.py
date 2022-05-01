import os.path


def check_secret(secret):
    if not secret.isdigit():
        raise IOError("Error, the secret must be a number")


def check_amount_people(amount_people):
    if amount_people < 0:
        raise IOError("Error, the amount of people must be positive.")
    if amount_people < 2:
        raise IOError("Error, there must be at least 2 people.")


def check_file(file):
    if not os.path.isfile(file):
        raise IOError(f"Error, the file '{file}' do not exist.")
    if not file.endswith(".txt"):
        raise IOError(f"Error, the file '{file}' must be a txt.")


def check_mail(mail):
    if not mail.endswith("gmail.com"):
        raise IOError("Error, the mail given must be a gmail.")


def check_minimum_people(amount_people, minimum_people):
    if minimum_people < 0:
        raise IOError(f"Error, the number of number of the minimum number of  people to retrieve the secret must be "
                      f"positive.")
    if amount_people < 2:
        raise IOError("Error, there must be at least 2 people.")
    if minimum_people > amount_people:
        raise IOError(f"Error, the number of the minimum number of people"
                      f" to retrieve the secret ({minimum_people}) can not be greater than the amount of people ({amount_people}).")


def check_key(key):
    if 'k' not in key:
        raise IOError(f"Error, the key entered is incorrect must contain a 'k'.")
    portions = key.split('k')
    if len(portions[0]) < 1 or len(portions[1]) < 1 or not portions[1].isdigit() or not portions[0].isdigit():
        raise IOError(f"Error, the key entered is incorrect.")
