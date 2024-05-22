import logging

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

from function_assistants import func_handler

logging.basicConfig(level=logging.INFO)


class AsymmetricAlgorithm:
    """
    cipher-class for asymmetric operations has methods for generating keys,
    encrypt data and decrypting it using cryptography module
    """

    def __init__(self, private_key_path: str, public_key_path: str) -> None:
        """
        init-method with private_key_path and public_key_path
        """
        self.private_key_path = private_key_path
        self.public_key_path = public_key_path

    @staticmethod
    @func_handler
    def generate_key_pair(key_size: int) -> tuple:
        """
        method generate key using rsa from cryptography
        """
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_size)
        public_key = private_key.public_key()
        return private_key, public_key

    @func_handler
    def serialize_private_key(self, private_key: rsa.RSAPrivateKey) -> None:
        """
        method serialize private key
        """
        with open(self.private_key_path, 'wb') as key_file:
            key_file.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                     encryption_algorithm=serialization.NoEncryption()))

    @func_handler
    def serialize_public_key(self, public_key: rsa.RSAPublicKey) -> None:
        """
        method serialize public key
        """
        with open(self.public_key_path, 'wb') as key_file:
            key_file.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                   format=serialization.PublicFormat.SubjectPublicKeyInfo))

    @func_handler
    def deserialize_private_key(self) -> rsa.RSAPrivateKey:
        """
        method deserialize private key
        """
        with open(self.private_key_path, 'rb') as key_file:
            return serialization.load_pem_private_key(key_file.read(), password=None)

    @func_handler
    def deserialize_public_key(self) -> rsa.RSAPublicKey:
        """
        method deserialize public key
        """
        with open(self.public_key_path, 'rb') as key_file:
            return serialization.load_pem_public_key(key_file.read())

    @staticmethod
    @func_handler
    def encrypt_with_public_key(public_key: rsa.RSAPublicKey, text: bytes) -> bytes:
        """
        method encrypts text using public key
        """
        return public_key.encrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                     algorithm=hashes.SHA256(), label=None))

    @staticmethod
    @func_handler
    def decrypt_with_private_key(private_key: rsa.RSAPrivateKey, ciphertext: bytes) -> bytes:
        """
        method decrypts text using private key
        """
        return private_key.decrypt(ciphertext, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                            algorithm=hashes.SHA256(), label=None))
