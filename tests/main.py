import masks, widget

def check_card_mask(card: int, result: str) -> bool:
    """Проверка функции маскировки карты"""
    masked_card = masks.get_mask_card_number(card)
    if masked_card == result:
        return True
    else:
        return False


def check_account_mask(account: int, result: str) -> bool:
    """Проверка функции маскировки аккаунта"""
    masked_account = masks.get_mask_account(account)
    if masked_account == result:
        return True
    else:
        return False


if __name__ == "__main__":
    print(check_card_mask(7000792289606361, "7000 79** **** 6361"))
    print(check_account_mask(73654108430135874305, "**4305"))

print(widget.mask_account_card('Visa Platinum 7000792289606361'))
print(widget.mask_account_card('Счет 64686473678894779589'))