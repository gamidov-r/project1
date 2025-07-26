import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
URL = "https://api.apilayer.com/exchangerates_data/convert"

# DEBUG = True  # возврат заглушки, минуя работу с api
DEBUG = False  # работа напрямую с api


mock = {
    "success": True,
    "query": {"from": "EUR", "to": "RUB", "amount": 5},
    "info": {"timestamp": 1753524555, "rate": 93.035614},
    "date": "2025-07-26",
    "result": 465.17807,
}


def convert_currency(current: str, to: str, value: float) -> dict:
    """Конвертация валюты через API, ответ в виде json запроса"""
    if DEBUG:
        return mock
    params = {"from": current, "to": to, "amount": value, "apikey": API_KEY}
    response = requests.get(URL, params)
    json_response = response.json()
    if json_response["success"]:
        return json_response
    else:
        return {}
