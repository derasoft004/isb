"""
это самое
"""

RU_ALPH = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def read_file(file_name: str) -> str:
    """
    reading file

    :param file_name: path to file
    :return:  string in one line (withoun \n)
    """
    try:
        return ''.join(open(file_name, 'r').readlines()) # .replace('\n', '   ')
    except Exception as e:
        return 'reading error:' + str(e)


def write_file(file_name: str, data: str) -> None:
    """
    writing to file

    :param file_name: path to file
    :param data: data for writing
    :return None:
    """
    try:
        open(file_name, 'w').write(data) # .replace('   ', '\n')
    except Exception as e:
        print(e)


def rot16(string: str) -> str:
    return ''.join(map(lambda c: chr(ord(c) + 16) if c.isalpha() and c.lower() <= 'п' else
                                 chr(ord(c) - 16) if c.isalpha() else c, string))


def task_1(file_to_read: str, file_to_write: str) -> None:
    """
    writing encrypted text to file using function rot16

    :param file_to_read:
    :param file_to_write:
    :return:
    """
    write_file(file_to_write, rot16(read_file(file_to_read)))


def global_symbols_frequency() -> dict:
    """

    :return:
    """
    frequency_lst = [i.replace('§', ' ') for i in read_file('task_2/frequency_symbols_based.txt').split('\n')]
    dictionary = dict()
    symbols, frequency = \
        [frequency_lst[i][0] for i in range(len(frequency_lst))], \
        [float(frequency_lst[i][4:12]) for i in range(len(frequency_lst))]

    for ind, key in enumerate(symbols):
        dictionary[key] = frequency[ind]
    return dictionary


def encrypted_text_symbols_frequency() -> dict:
    """
    complete dictionary with symbols frequency in the text

    :return: text's symbols dictionary
    """
    encrypted_text = read_file('task_2/cod8.txt')
    symbols_dict = dict()
    for key in set(encrypted_text):
        symbols_dict[key] = float(round(encrypted_text.count(key) / len(encrypted_text), 6))
    return symbols_dict


def get_equals_dict() -> dict:
    gsf = global_symbols_frequency()
    etsf = encrypted_text_symbols_frequency()

    s_encrypted_text_frequency = sorted(etsf.values(), reverse=True)

    sorted_text_dict = dict()
    for frequency in s_encrypted_text_frequency:
        for etsf_key in etsf.keys():
            if etsf[etsf_key] == frequency:
                sorted_text_dict[etsf_key] = frequency
    # print(gsf, '\n\n', sorted_text_dict, '\n\n', )

    sorted_text_dict.pop('-')
    equals_dict = dict()
    i = 0
    for etsf_key in sorted_text_dict.keys():
        j = 0
        for gsf_key in gsf.keys():
            j += 1
            equals_dict[etsf_key] = gsf_key
            if j > i: break

        i += 1

    print(gsf, '\n\n', sorted_text_dict, '\n\n', equals_dict)

    return equals_dict


def task_2():
    encrypted_text = read_file('task_2/cod8.txt')
    ret_str = ''
    symbols = get_equals_dict()
    for symbol in encrypted_text:
        try:
            ret_str += symbols[symbol]
        except KeyError:
            ret_str += symbol
    print(ret_str)

    # TODO
    #  генерируются расшифрованные варианты, но они 99/100 не верные (число приведено для наглядности), тк в памяти
    #  в хеш таблице sorted_text_dict элементы расположены рандомно


def main() -> None:
    # task_1('task_1/common_text.txt', 'task_1/cod8.txt')
    task_2()


if __name__ == '__main__':
    main()




































