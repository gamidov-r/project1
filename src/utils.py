import json
from typing import Union

import external_api

OPERATIONS_PATH = "../data/operations.json"


def load_operations(json_path: str) -> dict[str, Union]:
    """Чтение json файла"""
    try:
        with open(json_path, "r", encoding='UTF-8') as f:
            return json.load(f)
    except json.JSONDecoder:
        return {}


def get_amount(transaction: dict) -> float:
    """Получение суммы транзакции в рублях"""
    data = transaction.get("operationAmount")
    if data is None:
        return 0.0
    if data["currency"]["code"] == "RUB":
        return float(data["amount"])
    else:
        from_api = external_api.convert_currency(data["currency"]["code"], "RUB", data["amount"])
        return float(from_api["result"])


# transactions = load_operations(OPERATIONS_PATH)
# print(transactions)
# for item in transactions:
#     print(get_amount(item))
