from unittest.mock import Mock

from src.pd_transactions import *

TRANS_CSV = "data/transactions.csv"
TRANS_XLSX = "../data/transactions_excel.xlsx"

resp = {
    "id": "650703",
    "state": "EXECUTED",
    "date": "2023-09-05T11:30:32Z",
    "amount": "16210",
    "currency_name": "Sol",
    "currency_code": "PEN",
    "from": "Счет 58803664561298323391",
    "to": "Счет 39745660563456619397",
    "description": "Перевод организации",
}, {
    "id": "3598919",
    "state": "EXECUTED",
    "date": "2020-12-06T23:00:58Z",
    "amount": "29740",
    "currency_name": "Peso",
    "currency_code": "COP",
    "from": "Discover 3172601889670065",
    "to": "Discover 0720428384694643",
    "description": "Перевод с карты на карту",
}


def test_read_transactions_csv():
    mock_load = Mock(return_value=resp)
    assert read_transactions_csv(TRANS_CSV)[0] == mock_load()[0]


def test_read_transactions_excel():
    mock_load = Mock(return_value=resp)
    read_transactions_excel = mock_load
    assert read_transactions_excel(TRANS_XLSX)[0] == mock_load()[0]
