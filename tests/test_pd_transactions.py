from unittest.mock import Mock
from unittest.mock import patch

from src.pd_transactions import *

TRANS_CSV = '../data/transactions.csv'
TRANS_XLSX = '../data/transactions_excel.xlsx'

resp=''
def test_read_transactions_csv():
    mock_load = Mock(return_value=resp)
    json.load = mock_load
    assert load_operations("data/operations.json") == resp



def test_read_transactions_excel():
    pass




print(read_transactions_csv(TRANS_CSV))
print(read_transactions_excel(TRANS_XLSX))
