import sys

from constants import CARD_HASH, LAST_NUMS, BINS
from card_handler import multy_brut_card_number

def main():
    multy_brut_card_number(BINS, CARD_HASH, LAST_NUMS, 8)


if __name__ == "__main__":
    main()

