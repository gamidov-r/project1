def mask_account_card(txt: str) -> str:
    """Маскировка номера карты и счета звездочками"""
    card = txt.split(" ")[-1]
    if len(card) == 16:
        tmp = str(card).replace(str(card)[6:12], "******")
        lst = list(tmp)
        lst.insert(12, " ")
        lst.insert(8, " ")
        lst.insert(4, " ")
        masked_card = "".join(lst)
    elif len(card) > 16:
        masked_card = "**" + str(card)[-4:]
    return txt.replace(card, masked_card)


def get_date(date_time: str) -> str:
    """Преобразовывание даты в другой формат"""
    date = date_time.split("T")[0]
    year, month, day = date.split("-")
    return "{}.{}.{}".format(day, month, year)
