import collections
import csv
import re

import src.masks as masks
import src.widget as widget

sort_by_date, ascending, only_rub, choiced_filter = 0, 0, 0, 0


def check_card_mask(card: int, result: str) -> bool:
    """Проверка функции маскировки карты"""
    masked_card = masks.get_mask_card_number(card)
    if masked_card == result:
        return True
    else:
        return False


def check_account_mask(account: int, result: str) -> bool:
    """Проверка функции маскировки аккаунта"""
    masked_account = masks.get_mask_account(account)
    if masked_account == result:
        return True
    else:
        return False


def process_bank_search(data: list[dict], search: str) -> tuple[list[dict], list[str]]:
    """Функция фильтрации и сортировки транзакций по заданным пользователем критериям"""
    filtered_trans = []
    count_trans = []
    # search = "перевод со счета"
    if " " in search:
        pattern = re.compile(r"\s+")
        split_text = pattern.split(search)
        split_text.sort(reverse=True, key=lambda x: len(x))
        search_pattern = r"({} (.)+ {}) | ({} (.)+ {}) | ({} {}) | ({} {})".format(
            re.escape(split_text[0]),
            re.escape(split_text[1]),
            re.escape(split_text[1]),
            re.escape(split_text[0]),
            re.escape(split_text[0]),
            re.escape(split_text[1]),
            re.escape(split_text[1]),
            re.escape(split_text[0]),
        )
    else:
        search_pattern = r"{}".format(re.escape(search))
    if sort_by_date:
        data.sort(reverse=ascending, key=lambda x: x.get("date"))

    for item in data:
        if not item["state"] == choiced_filter:
            continue
        if only_rub:
            if not item["currency"]["code"] == "RUB":
                continue
        desc = item["description"]
        status = re.findall(search_pattern, desc, re.IGNORECASE)
        if len(status) > 0:
            filtered_trans.append(item)
            count_trans.append(item["id"])
    return filtered_trans, count_trans


def main() -> None:
    """Основная функция по получению параметров сортировки от пользователя"""
    welcome = """Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
    # global sort_by_date, ascending, only_rub, choiced_filter
    file_types = {"1": "json", "2": "csv", "3": "xlsx"}
    print(welcome)
    x = input("Пользователь: ")
    # x = "3"
    if x in file_types:
        print(f"Программа: Для обработки выбран {file_types[x].upper()}-файл.")
    else:
        print("Программа: Ответ не совпадает с вариантами! Выберите правильный вариант, указав число 1, 2, или 3!")
        main()
    filter_message = """Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
    filter_types = ["EXECUTED", "CANCELED", "PENDING"]
    while 1:
        print(filter_message)
        x = input("Пользователь: ").upper()
        # x = "EXECUTED"
        if x in filter_types:
            print(f"Программа: Операции отфильтрованы по статусу {x}")
            choiced_filter = x
            break
        else:
            print(f'Программа: Статус операции "{x}" недоступен.')

    questions = [
        "Отсортировать операции по дате? Да/Нет",
        "Отсортировать по возрастанию или по убыванию?",
        "Выводить только рублевые транзакции? Да/Нет",
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет",
        "Распечатываю итоговый список транзакций...",
    ]

    pattern_yes = r"(да|yes|lf|нуы|1)"
    pattern_no = r"(Нет|ytn|no|тщ|0)"
    pattern_ascending = r"(возр|djph|фысутв|ascend)"
    pattern_descending = r"(убыв|e,sd|вуысутв|descend)"

    print(f"Программа: {questions[0]}")
    x = input("Пользователь: ")
    # x = "нет"
    if pattern_yes in re.findall(pattern_yes, x, re.IGNORECASE):
        sort_by_date = 1
    elif pattern_no in re.findall(pattern_no, x, re.IGNORECASE):
        sort_by_date = 0

    print(f"Программа: {questions[1]}")
    x = input("Пользователь: ")
    # x = "возраст"
    if pattern_ascending in re.findall(pattern_ascending, x, re.IGNORECASE):
        ascending = 1
    elif pattern_descending in re.findall(pattern_descending, x, re.IGNORECASE):
        ascending = 0

    print(f"Программа: {questions[2]}")
    x = input("Пользователь: ")
    # x = "нет"
    if pattern_yes in re.findall(pattern_yes, x, re.IGNORECASE):
        only_rub = 1
    elif pattern_no in re.findall(pattern_no, x, re.IGNORECASE):
        only_rub = 0

    print(f"Программа: {questions[3]}")
    x = input("Пользователь: ")
    # x = "нет"
    print(f"Программа: {questions[4]}")
    result, trans_ids = process_bank_search(read_transactions_csv("../data/transactions.csv"), "Перевод")
    print(result)
    print(f"Программа\nВсего банковских операций в выборке: {collections.Counter(trans_ids).total()}")
    if result:
        for item in result:
            print(
                f"{widget.get_date(item["date"])}\n{masks.get_mask_account(item["from"])}\nСумма: {item["amount"]} {item["currency_name"]}\n"
            )
    else:
        print("Транзакций не найдено")


def read_transactions_csv(path_to_csv: str) -> list:
    """чтение csv из файла"""
    with open(path_to_csv, encoding="UTF-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        trans_list = []
        for row in reader:
            trans_list.append(row)
        return trans_list


if __name__ == "__main__":
    main()
    # print(check_card_mask(7000792289606361, "7000 79** **** 6361"))
    # print(check_account_mask(73654108430135874305, "**4305"))
