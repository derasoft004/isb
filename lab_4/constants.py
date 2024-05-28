from functions_assistans import load_json

CARD_INFO_PATH = 'cards_info.json'

dict_cards_information = load_json(CARD_INFO_PATH)

CARD_HASH = dict_cards_information["hash"]
PAYMENT_SYSTEM = dict_cards_information["payment_system"]
TYPE_CARD = dict_cards_information["type_card"]
BANK_NAME = dict_cards_information["bank_name"]
LAST_NUMS = dict_cards_information["last_nums"]
HASH_ALGORITHM = dict_cards_information["hash_algorithm"]
BINS = dict_cards_information["bins"]
