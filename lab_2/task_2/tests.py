from math import erfc
from mpmath import gammainc

from constants import *
from functions_assistant import tests_handler, substring_in_sentence, file_reader


@tests_handler
def frequency_bit_test(sequence: str) -> float:
    """
    the function calculates bit's frequency in bits sequence
    :param sequence: bit sequence
    :return: p_value - special sequence's bit frequency
    """
    s_n = abs(sum(1 if el == '1' else -1 for el in sequence)) / N ** 0.5
    p_value = erfc(s_n / 2 ** 0.5)
    return p_value


@tests_handler
def identical_consecutive_bits(sequence: str) -> float:
    """
    the function searches for sequences of identical bits and calculates the P-value
    using some formulas and the math.erfc() method.
    :param sequence: bit sequence
    :return: p_value - special identical bits coefficient
    """
    p_value = 0
    ones_rate = sequence.count('1') / N
    if abs(ones_rate - 1 / 2) < 2 / N ** 0.5:
        Vn = 0
        for ind in range(1, N):
            if sequence[ind] != sequence[ind - 1]:
                Vn += 1
        p_value = erfc(abs(Vn - 2 * N * ones_rate * (1 - ones_rate)) /
                       (2 * (2 * N) ** 0.5 * ones_rate * (1 - ones_rate)))

    return p_value


@tests_handler
def longest_sequence_of_ones_in_block(sequence: str) -> float:
    """
    firstly calculating statics substrings with different lengths, next calculating 'xi' -
    distribution of the sum of squares of independent random variables
    and in the end - calculating p_value using incomplete gama function from mpmath library
    :param sequence: bit sequence
    :return: p_value - special coefficient longest substrings of ones
    """
    max_length_values_dict = dict((str(i), 0) for i in range(1, 5))
    for block in range(int(N/M)):
        portion = sequence[block * 8:(block + 1) * 8:]
        max_length_in_block = substring_in_sentence(portion)
        max_length_values_dict[str(max_length_in_block)] += 1

    pi_list, xi = [P0, P1, P2, P3], 0
    for ind in range(4):
        pi, elem = pi_list[ind], max_length_values_dict[str(ind + 1)]
        xi += ((elem - 16 * pi) ** 2) / (16 * pi)

    return gammainc(3 / 2, xi / 2)


if __name__ == '__main__':
    print('TEST 1 (java sequence):', frequency_bit_test(file_reader(PATH_CPP_PNG)),
          '\nTEST 1 (c++ sequence):', frequency_bit_test(file_reader(PATH_JAVA_PNG)))
    print('TEST 2 (java sequence):', identical_consecutive_bits(file_reader(PATH_CPP_PNG)),
          '\nTEST 2 (c++ sequence):', identical_consecutive_bits(file_reader(PATH_JAVA_PNG)))
    print('TEST 3 (java sequence):', longest_sequence_of_ones_in_block(file_reader(PATH_CPP_PNG)),
          '\nTEST 3 (c++ sequence):', longest_sequence_of_ones_in_block(file_reader(PATH_JAVA_PNG)))
