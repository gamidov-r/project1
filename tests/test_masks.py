import pytest
import masks

# get_mask_account', 'get_mask_card_number'

@pytest.mark.parametrize("card, expected", [('0123 2345 4567 6789', '**6789'), ('0987654321234567', '**4567'), ('', '**')])
def test_get_mask_account(card, expected):
    assert masks.get_mask_account(card)  == expected

def test_get_mask_account_via_assert():
    assert masks.get_mask_account('0123 2345 4567 6789') == '**6789'
    assert masks.get_mask_account('0987654321234567') == '**4567'
    assert masks.get_mask_account('') == '**'



