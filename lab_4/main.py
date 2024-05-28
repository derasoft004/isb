from multiprocessing import cpu_count
import hashlib

from constants import CARD_HASH, LAST_NUMS, HASH_ALGORITHM, BINS


CPU_COUNT = cpu_count()

print(hashlib.algorithms_available)

