import pytest

import widget


@pytest.mark.parametrize(
    "card, expected",
    [("1234345656787890", "1234 34** **** 7890"), ("1321123123123123123123123123123123123123", "**3123"), ("", "**")],
)
def test_mask_account_card(card, expected):
    assert widget.mask_account_card(card) == expected


@pytest.mark.parametrize("date, expected", [("2016-20-14", "14.20.2016"), ("1984-12-20T2:30:10", "20.12.1984")])
def test_get_date(date, expected):
    assert widget.get_date(date) == expected
