from typing import Generator


def filter_by_currency(transactions: dict, code: str) -> Generator:
    """Обработка списка словарей, фильтрация по ключу (типу валюты)"""
    filtered_trans = list(filter(lambda x: x.get("operationAmount").get("currency").get("code") == code, transactions))
    # print(list(filtered_trans))
    for index in range(len(list(filtered_trans))):
        yield filtered_trans[index]


def transaction_descriptions(transactions: dict) -> Generator:
    """генерация описаний к транзакциям"""
    for item in transactions:
        yield item.get("description")


def card_number_generator(start: int, stop: int) -> Generator:
    """генерация номеров карт с заданным промежутком в порядке возрастания"""
    if start >= stop:
        yield "error"
    for index in range(start, stop + 1):
        yield "0000 0000 0000 0000"[: -len(str(index))] + str(index)
