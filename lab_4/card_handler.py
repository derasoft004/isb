import logging

import hashlib
from multiprocessing import Pool

from functions_assistans import func_handler


class CardHandler:
    def __init__(self, hash_string: str, bins_cards: list, last_nums: int):
        """
        initial-method with hash_string and last_nums from technical task, bins_cards for alfa bank
        """
        self.hash_string: str = hash_string
        self.bins_cards: list = bins_cards
        self.last_nums: int = last_nums

    @func_handler
    def brut_card_hashes(self, center_nums: int) -> str:
        """
        method for bruteforce nums while don't find a match hash
        """
        for bin_card in self.bins_cards:
            some_card = f'{str(bin_card)}{str(center_nums).zfill(6)}{str(self.last_nums)}'
            hashed_card = str(hashlib.sha3_256(some_card.encode()).hexdigest())
            if hashed_card == self.hash_string:
                return some_card

    @staticmethod
    @func_handler
    def multy_brut_card_number(count_cpu: int) -> str:
        """
        method uses multiprocessing for faster bruteforce nums into the card's values
        """
        with Pool(count_cpu) as pool:
            for finally_card in pool.map(CardHandler.brut_card_hashes, [center_num for center_num in range(1_000_000)]):
                if finally_card:
                    logging.info(f"Current card's number is: {finally_card}.")
                    pool.terminate()
                    return finally_card

