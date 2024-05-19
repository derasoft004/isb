import logging

from symmetric_algorithm import SymmetricAlgorithm
from asymmetric_algorithm import AsymmetricAlgorithm
from function_assistants import FileAssistant, func_handler

logging.basicConfig(level=logging.INFO)


class HybridSystem:
    """
    class with tasks for doing encryption using symmetric and asymmetric keys
    """

    def __init__(self, text_path: str, symmetric_key_path: str,
                 encrypted_text_path: str, decrypted_text_path: str,
                 symmetric_crypto: SymmetricAlgorithm, asymmetric_crypto: AsymmetricAlgorithm) -> None:
        self.text_path = text_path
        self.symmetric_key_path = symmetric_key_path
        self.encrypted_text_path = encrypted_text_path
        self.decrypted_text_path = decrypted_text_path
        self.symmetric_crypto = symmetric_crypto
        self.asymmetric_crypto = asymmetric_crypto

    @func_handler
    def generate_keys(self) -> None:
        """
        method generate asymmetric and symmetric keys
        """
        symmetric_key = self.symmetric_crypto.generate_key()
        private_key, public_key = self.asymmetric_crypto.generate_key_pair(2048)

        self.asymmetric_crypto.serialize_private_key(private_key)
        self.asymmetric_crypto.serialize_public_key(public_key)

        encrypted_symmetric_key = self.asymmetric_crypto.encrypt_with_public_key(public_key, symmetric_key)
        key = FileAssistant(f"{self.symmetric_key_path[:-4]}_{self.symmetric_crypto.key_len}.txt")
        key.serialize_key(encrypted_symmetric_key)

        logging.info("Keys generated and serialize to files 'symmetric.txt', 'public.pem', 'private.pem'.")

    @func_handler
    def encrypt_text(self) -> None:
        """
        method encrypt text using the generated symmetric key
        """
        key = FileAssistant(f"{self.symmetric_key_path[:-4]}_{self.symmetric_crypto.key_len}.txt")
        symmetric_key = key.deserialize_key()
        symmetric_key = self.asymmetric_crypto.decrypt_with_private_key(
            self.asymmetric_crypto.deserialize_private_key(), symmetric_key)
        text_file = FileAssistant(self.text_path)
        plaintext = bytes(text_file.read_text_file("r", "UTF-8"), "UTF-8")
        encrypted_text = self.symmetric_crypto.encrypt_text(symmetric_key, plaintext)
        enc_file = FileAssistant(self.encrypted_text_path)
        enc_file.write_text_file(encrypted_text)
        logging.info("Message encrypted and written to file 'encrypted_text.txt'.")


    def decrypt_text(self) -> None:
        """
        method decrypts text using the generated symmetric key
        """
        sym_key = FileAssistant(f"{self.symmetric_key_path[:-4]}_{self.symmetric_crypto.key_len}.txt")
        symmetric_key = sym_key.deserialize_key()
        symmetric_key = self.asymmetric_crypto.decrypt_with_private_key(
            self.asymmetric_crypto.deserialize_private_key(), symmetric_key)
        enc_file = FileAssistant(self.encrypted_text_path)
        encrypted_text = bytes(enc_file.read_text_file("rb"))
        decrypted_text = self.symmetric_crypto.decrypt_text(symmetric_key, encrypted_text)
        dec_file = FileAssistant(self.decrypted_text_path)
        dec_file.write_text_file(decrypted_text)
        logging.info("Message decrypted and written to file 'decrypted_text.txt'.")
