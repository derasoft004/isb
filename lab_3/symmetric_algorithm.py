import logging
import os
import warnings

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.utils import CryptographyDeprecationWarning

from function_assistants import func_handler

logging.basicConfig(level=logging.INFO)
warnings.filterwarnings("ignore")


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

    @staticmethod
    @func_handler
    def encrypt_text(symmetric_key: bytes, text: bytes) -> bytes:
        """
        method encrypts text using symmetric key
        """
        iv = os.urandom(8)
        cipher = Cipher(algorithms.Blowfish(symmetric_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        padded_text = padder.update(text) + padder.finalize()
        return iv + encryptor.update(padded_text) + encryptor.finalize()


    @staticmethod
    @func_handler
    def decrypt_text(symmetric_key: bytes, encrypted_text: bytes) -> bytes:
        """
        method decrypts text using symmetric key
        """
        iv = encrypted_text[:8]
        encrypted_text = encrypted_text[8:]
        cipher = Cipher(algorithms.Blowfish(symmetric_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        return unpadder.update(decrypted_text) + unpadder.finalize()
