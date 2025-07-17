from typing import Generator


def filter_by_currency(transactions: dict, code: str) -> Generator:
    filtered_trans = list(filter(lambda x: x.get("operationAmount").get("currency").get("code") == code, transactions))
    # print(list(filtered_trans))
    for index in range(len(list(filtered_trans))):
        yield filtered_trans[index]


def transaction_descriptions(transactions: dict) -> Generator:
    for item in transactions:
        yield item.get("description")


def card_number_generator(first: int, last: int) -> Generator:
    if first >= last:
        yield "error"
    for index in range(first, last + 1):
        yield "0000 0000 0000 0000"[: -len(str(index))] + str(index)
