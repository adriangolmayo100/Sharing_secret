from input import checker, input_application
import utils


def run(keys):
    secret = reveal_secret(keys)
    return secret


def request_data():
    amount_people = input_application.request_amount_people()
    checker.check_amount_people(amount_people)
    keys = input_application.request_keys(amount_people)
    return amount_people, keys


def reveal_secret(keys):
    points = utils.keys_to_points(keys)
    polynomial = utils.interpolation_lagrange(points)
    return utils.get_secret(polynomial)
