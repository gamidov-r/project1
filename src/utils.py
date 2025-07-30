import json
import logging
from typing import Union

import external_api

OPERATIONS_PATH = "../data/operations.json"

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] - %(filename)s - %(levelname)s : %(message)s",
    filename="../logs/utils.log",
    filemode="w",
)

amount_logger = logging.getLogger("utils.amount")
json_logger = logging.getLogger("utils.json")


def load_operations(json_path: str) -> dict[str, Union]:
    """Чтение json файла"""
    try:
        with open(json_path, "r", encoding="UTF-8") as f:
            json_logger.debug(f"Успешное чтение json файла: {json_path}")
            return json.load(f)
    except json.JSONDecoder:
        json_logger.error(f"Ошибка чтения json файла: {json_path}")
        return {}


def get_amount(transaction: dict) -> float:
    """Получение суммы транзакции в рублях"""
    data = transaction.get("operationAmount")
    if data is None:
        amount_logger.error("Ошибка парсинга транзакции: пустая или не содержит нужных ключей")
        return 0.0
    if data["currency"]["code"] == "RUB":
        amount_logger.debug("Успешное получение суммы транзакции, приведенной в рублях")
        return float(data["amount"])
    else:
        from_api = external_api.convert_currency(data["currency"]["code"], "RUB", data["amount"])
        amount_logger.debug(f'Успешное получение суммы транзакции, приведенной в {data["currency"]["code"]}')
        return float(from_api["result"])


# transactions = load_operations(OPERATIONS_PATH)
# print(transactions)
# for item in transactions:
#     print(get_amount(item))
