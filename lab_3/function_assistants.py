import json
import logging

logging.basicConfig(level=logging.INFO)


def func_handler(func):
    """
    handler that get a function and put it into try-except construction for catching errors
    """
    try:
        return func
    except Exception as e:
        logging.error(f'Error from {func.__name__} function: {e}\n')


class FileAssistant:
    def __init__(self, path: str) -> None:
        self.path = path

    @func_handler
    def serialize_key(self, key: bytes) -> None:
        """
        method serializes the key and save it to a file.
        """
        with open(self.path, 'wb') as key_file:
            key_file.write(key)

    @func_handler
    def deserialize_key(self) -> bytes:
        """
        method deserializes the key from a file.
        """
        with open(self.path, 'rb') as key_file:
            return key_file.read()

    @func_handler
    def read_text_file(self, mode: str, encoding=None) -> str:
        """
        method reads text from a file.
        """
        with open(self.path, mode=mode, encoding=encoding) as file:
            return file.read()

    @func_handler
    def write_text_file(self, text: str) -> None:
        """
        method writes text to a file.
        """
        with open(self.path, 'wb') as file:
            file.write(text)

    @func_handler
    def read_json_file(self) -> dict:
        """
        method reads json file
        """
        with open(self.path, 'r', encoding='utf-8') as f:
            paths = json.load(f)
        return paths