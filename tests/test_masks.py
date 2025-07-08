import pytest
import masks


def test_get_mask_account_via_assert():
    assert masks.get_mask_account('test name') == '**name'
    assert masks.get_mask_account('HelloWorld') == '**orld'
    assert masks.get_mask_account('') == '**'


@pytest.mark.parametrize("card, expected", [('test name', '**name'), ('HelloWorld', '**orld'), ('', '**')])
def test_get_mask_account(card, expected):
    assert masks.get_mask_account(card)  == expected


@pytest.mark.parametrize("number, expected", [('0123 2345 4567 6789', '0123 23** **** 6789'), ('0987654321234567', '0987 65** **** 4567'), (1928374657489123, '1928 37** **** 9123'), ('', '**** **  ')])
def test_get_mask_card_number(number, expected):
    assert masks.get_mask_card_number(number)  == expected
