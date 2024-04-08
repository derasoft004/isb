import json
import logging


def load_json(file_name: str) -> dict:
    """
    func for reading .json file
    """

    with open(file_name, 'r') as file:
        return json.load(file)


def file_reader(path_file: str) -> str:
    """
    func for reading .txt files
    """
    with open(path_file, 'r') as file:
        return file.readline().replace(' ', '')


def tests_handler(func):
    """
    handler that get a function and put it into try-except construction for catching errors
    :param func: the function that will run tests
    :return: function if running is access else logging
    """
    try:
        return func
    except Exception as e:
        logging.error(f'Error from {func.__name__} function: {e}\n')


def substring_in_sentence(sequence: str) -> int:
    """
    the function helper for finding max length of substring from sequence
    :param sequence: bit sequence
    :return: max length of substring
    """
    max_len, cur_len = 0, 0

    for symbol in sequence:
        if symbol == '1':
            cur_len += 1
        else:
            max_len = max(max_len, cur_len)
            cur_len = 0

    max_len = max(max_len, cur_len)

    return max_len if max_len < 4 else 4

