import json
import logging

logging.basicConfig(level=logging.INFO)


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


class FileAssistant:
    def __init__(self, path: str) -> None:
        self.path = path

    @func_handler
    def read_text_file(self, mode: str, encoding=None) -> str:
        """
        Read text from a file.
        :param mode: The mode to open the file in.
        :param encoding: (str, optional) The encoding of the text file. Defaults to None .

        :return: The content of the text file.
        """
        with open(self.path, mode=mode, encoding=encoding) as file:
            return file.read()

    @func_handler
    def write_text_file(self, text: str) -> None:
        """
        Write text to a file.

        :param text: The text to write to the file.
        """
        with open(self.path, 'wb') as file:
            file.write(text)

    @func_handler
    def read_json_file(self) -> dict:
        with open(self.path, 'r', encoding='utf-8') as f:
            paths = json.load(f)
        return paths