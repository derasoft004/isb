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
    counter_dict = dict((str(i), 0) for i in range(1, 5))
    count, max_len = 0, 1
    sequence_not_null = False

    def adder(c):
        if c in range(1, 5):
            counter_dict[str(c)] += 1
        elif c >= 5:
            counter_dict['4'] += 1

    for ind in range(len(sequence)):
        if int(sequence[ind]):
            sequence_not_null = True
            count += 1
        else:
            adder(count)
            count = 0
    if sequence_not_null:
        adder(count)
        max_len = max(int(key) for key, value in counter_dict.items() if value)
    return max_len
