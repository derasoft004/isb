import logging

import hashlib
from multiprocessing import Pool

from functions_assistans import func_handler, dump_json


@func_handler
def brut_card_hashes(bins_cards: list, hash_string: str, last_nums: int, center_num: int) -> str:
    """
    func for bruteforce nums while don't find a match hash
    """
    for bin_card in bins_cards:
        some_card = f'{str(bin_card)}{str(center_num).zfill(6)}{str(last_nums)}'
        hashed_card = str(hashlib.sha3_256(some_card.encode()).hexdigest())
        if hashed_card == hash_string:
            return some_card


@func_handler
def multy_brut_card_number(bins_cards: list, hash_string: str, last_nums: int, count_cpu: int) -> str:
    """
    func uses multiprocessing for faster bruteforce nums into the card's values
    """
    with Pool(count_cpu) as pool:
        for finally_card in pool.starmap(brut_card_hashes,
                                         [(bins_cards, hash_string, last_nums, center_num)
                                          for center_num in range(1_000_000)]):
            if finally_card:
                logging.info(f"Current card's number is: {finally_card}.")
                pool.terminate()
                return finally_card
        logging.info("Current card's number wasn't find")


def algorithm_luna(card_number: str) -> bool:
    """
    algorithm Luna divides the sentence nums to even and odd and every odd is multiplied by 2
    next step function check is it more than 9 or not, if it's function adds numbers of current num (multiplied by 2)
    and adds finally numbers to returned sum
    func returns True, if returned sum mod 10 = 0.
    """
    return_num = 0
    for ind, elem in enumerate(card_number):
        cur_letter = int(elem)
        if not ind % 2:
            cur_letter *= 2
            tmp_num = cur_letter
            if cur_letter > 9:
                cur_letter = tmp_num % 10 + 1
        return_num += cur_letter

    if not return_num % 10:
        return True
    return False
