import pytest

import src.main as main

mock = [
    {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    },
    {
        "id": "3598919",
        "state": "EXECUTED",
        "date": "2020-12-06T23:00:58Z",
        "amount": "29740",
        "currency_name": "Peso",
        "currency_code": "COP",
        "from": "Discover 3172601889670065",
        "to": "Discover 0720428384694643",
        "description": "Перевод с карты на карту",
    },
]
search = "Перевод"


def test_process_bank_search():
    assert main.process_bank_search(mock, search) == ([], [])
    assert main.process_bank_search(mock, "test") == ([], [])