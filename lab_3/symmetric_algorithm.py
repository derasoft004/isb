import os

from function_assistants import func_handler


class SymmetricAlgorithm:
    """
    cipher-class for symmetric operations has methods for generating keys,
    encrypt data and decrypting it using cryptography module
    """

    def __init__(self, key_len: int) -> None:
        """
        init-method with key_len
        """
        self.key_len = key_len

    @func_handler
    def generate_key(self) -> bytes:
        """
        generate key using bytes from os module
        """
        return os.urandom(self.key_len // 8)


