from cryptography.hazmat.primitives.asymmetric import rsa

from function_assistants import func_handler


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






