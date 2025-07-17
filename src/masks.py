def get_mask_card_number(card: int) -> str:
    """Маскировка номера карты звездочками"""
    if len(str(card)) == 19: card = str(card).replace(' ', '')
    tmp = str(card).replace(str(card)[6:12], "******")
    lst = list(tmp)
    lst.insert(12, " ")
    lst.insert(8, " ")
    lst.insert(4, " ")
    return "".join(lst)


def get_mask_account(account: int) -> str:
    """Маскировка аккаунта"""
    return "**" + str(account)[-4:]
