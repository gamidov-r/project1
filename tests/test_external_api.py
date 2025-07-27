from unittest.mock import patch
from external_api import *

mock = {
    "success": True,
    "query": {"from": "EUR", "to": "RUB", "amount": 5},
    "info": {"timestamp": 1753524555, "rate": 93.035614},
    "date": "2025-07-26",
    "result": 465.17807,
}

def test_convert_currency():
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock
        assert convert_currency(current='EUR', to='RUB', value=5) == mock



