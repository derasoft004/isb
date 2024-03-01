"""
это самое
"""

RU_ALPH = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def read_file(file_name: str) -> str:
    """
    reading file
    :param file_name - path to file:
    :return string in one line (withoun \n):
    """
    return ''.join(open(file_name, 'r').readlines()).replace('\n', '§')


# print(read_file('task_1/common_text.txt'))


def write_file(file_name: str, data: str) -> None:
    """
    file to writing
    :param file_name:  path to file
    :param data: data for writing
    :return None:
    """
    try:
        open(file_name, 'w').write(data.replace('§', '\n'))
    except Exception as e:
        print(e)


def rot16(string: str) -> str:
    return ''.join(map(lambda c: chr(ord(c)+16) if c.isalpha() and c.lower() <= 'п' else
                                 chr(ord(c)-16) if c.isalpha() else c, string))

def task1(file_to_read: str, file_to_write: str) -> None:
    """
    записываем в файл зашифрованный текст
    :param file_to_read:
    :param file_to_write:
    :return:
    """
    write_file(file_to_write, rot16(read_file(file_to_read)))

task1('task_1/common_text.txt', 'task_1/encrypted_text.txt')






































