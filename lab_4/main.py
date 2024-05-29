import argparse

from multiprocessing import cpu_count

from constants import CARD_HASH, LAST_NUMS, BINS, FINALLY_CARD
from card_handler import multy_brut_card_number, algorithm_luna
from functions_assistans import func_handler, dump_json, load_json

@func_handler
def argparser():
    """
    parses command line arguments and returns the parsed arguments as a Namespace object.
    """
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-count', '--available_cores_count',
                       action='store_true',
                       help='Show count available machine\'s cores.')
    group.add_argument('-card', '--decryption_card_hash',
                       action='store_true',
                       help='Run decryption card hash using (default using 4 cores).')
    group.add_argument('-corr', '--correctness_cards_num',
                       action='store_true',
                       help='Check the correctness of cards number using algorithm Luna.')

    parser.add_argument('-card_num', '--cards_number',
                        type=str,
                        # default=FINALLY_CARD,
                        help='Use the card number or enter your own.')
    parser.add_argument('-ser', '--serialize_number',
                        type=str,
                        default=FINALLY_CARD,
                        help='Serialize the card numbers to the .json file.')
    parser.add_argument('-cores', '--count_using_cores',
                        type=int,
                        default=4,
                        help='Enter the count cores to multiprocessing (default uses 4 cores)')

    args = parser.parse_args()

    return args


@func_handler
def main():
    args = argparser()

    match args:
        case args if args.available_cores_count:
            print('Cores on your machine: ' + str(cpu_count()))

        case args if args.decryption_card_hash:
            cores_cur = args.count_using_cores
            finally_card = multy_brut_card_number(BINS, CARD_HASH, LAST_NUMS, cores_cur)
            if args.serialize_number:
                file_to_dump = args.serialize_number
                dump_json(file_to_dump, finally_card)

        case args if args.correctness_cards_num:
            if args.cards_number:
                card_number: str = args.cards_number
            else: card_number: str = load_json(FINALLY_CARD)
            print(card_number)
            if algorithm_luna(card_number):
                print('Your card is correctness.')
            else: print('Your card isn\'t correctness.')


if __name__ == "__main__":
    main()

