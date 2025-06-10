import re

PATH_WITH_ALL_NAMES = 'data/names.txt'
PATH_CYRILLIC_NAMES = 'data/cyrillic_names.txt'
PATH_LATIN_NAMES = 'data/latin_names.txt'


def read_names(path: str) -> list[str]:
    """ Чтение содержимого файла """
    with open(path, 'r', encoding='utf-8') as file:
        names = file.readlines()
        file.close()
    return names


def write_to_file(path: str, data: list) -> str:
    """ Запись данных в файл """
    with open(path, 'w') as file:
        file.write("\n".join(data))
    file.close()
    return "ok"


def filter_cyrillic_names(names: list[str]) -> list[str]:
    """ Фильтрация имен на кириллице """
    cyrillic_names = []
    cyrillic_pattern = r"[а-яА-Я]"
    for name in names:
        cyrillic_name = ''.join(re.findall(cyrillic_pattern, name))
        if len(cyrillic_name): cyrillic_names.append(cyrillic_name)
    return cyrillic_names


def filter_latin_names(names: list[str]) -> list[str]:
    """ Фильтрация имен на латинице """
    latin_names = []
    latin_pattern = r"[a-zA-Z]"
    for name in names:
        latin_name = ''.join(re.findall(latin_pattern, name))
        if len(latin_name): latin_names.append(latin_name)
    return latin_names


if __name__ == '__main__':
    names = read_names(PATH_WITH_ALL_NAMES)
    cyrillic_names = filter_cyrillic_names(names)
    latin_names = filter_latin_names(names)
    print("имена на кириллице ({}): {}".format(len(cyrillic_names), ", ".join(cyrillic_names)))
    print("имена на латинице ({}): {}".format(len(latin_names), ", ".join(latin_names)))
    # write_to_file(PATH_CYRILLIC_NAMES, cyrillic_names)
    # write_to_file(PATH_LATIN_NAMES, latin_names)
