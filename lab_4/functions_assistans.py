import json
import logging


def func_handler(func):
    """
    handler that get a function and put it into try-except construction for catching errors
    :param func: the function that will run tests
    :return: function if running is access else logging
    """
    try:
        return func
    except Exception as e:
        logging.error(f'Error from {func.__name__} function: {e}\n')


@func_handler
def load_json(file_name: str) -> dict | str:
    """
    func for reading .json file
    """

    with open(file_name, 'r') as file:
        return json.load(file)


@func_handler
def dump_json(path_file: str, string: str) -> None:
    """
    func for writing .txt files
    """
    with open(path_file, 'w') as file:
        json.dump(string, file)


@func_handler
def file_reader(path_file: str) -> str:
    """
    func for reading .txt files
    """
    with open(path_file, 'r') as file:
        return file.readline().replace(' ', '')


@func_handler
def file_writer(path_file: str, string: str) -> None:
    """
    func for writing .txt files
    """
    with open(path_file, 'w') as file:
        file.write(string)
