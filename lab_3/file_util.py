import json

from function_assistants import *


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
