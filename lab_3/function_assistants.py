import logging

from cryptography.utils import CryptographyDeprecationWarning

logging.basicConfig(level=logging.INFO)


def func_handler(func):
    """
    handler that get a function and put it into try-except construction for catching errors
    """
    try:
        return func
    except CryptographyDeprecationWarning:
        logging.error(f'In this version Blowfish marked as old type')
    except Exception as e:
        logging.error(f'Error from {func.__name__} function: {e}\n')
