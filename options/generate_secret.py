from input import input_application, read_file
import utils


def run(secret, amount_people, minimum_people):
    keys = generate_keys(secret, amount_people, minimum_people)
    return keys


def request_data(secret_in_file):
    if secret_in_file:
        file = input_application.request_file_secret()
        secret = read_file.first_line(file)
    else:
        secret = input_application.request_secret_terminal()
    amount_people = input_application.request_amount_people()
    minimum_people = input_application.request_minimum_to_recover(amount_people)
    return secret, amount_people, minimum_people


def generate_keys(secret, amount_people, minimum_people):
    polynomial = utils.polynomial_generator(minimum_people, secret)
    points = utils.get_points(polynomial, amount_people)
    keys = utils.points_to_keys(points)
    return keys
