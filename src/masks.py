import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] - %(filename)s - %(levelname)s : %(message)s",
    filename="../logs/masks.log",
    filemode="w",
)

card_logger = logging.getLogger("masks.card_number")
account_logger = logging.getLogger("masks.account")


def get_mask_card_number(card: int) -> str:
    """Маскировка номера карты звездочками"""
    try:
        if len(str(card)) == 19:
            card = str(card).replace(" ", "")
        tmp = str(card).replace(str(card)[6:12], "******")
        lst = list(tmp)
        lst.insert(12, " ")
        lst.insert(8, " ")
        lst.insert(4, " ")
        card_logger.debug("Маскировка номера карты прошла успешно")
        return "".join(lst)
    except Exception as err:
        card_logger.error(f"Ошибка при маскировке номера карты: {err}", exc_info=True)


def get_mask_account(account: int) -> str:
    """Маскировка аккаунта"""
    try:
        account_logger.debug("Успешная маскировка аккаунта")
        return "**" + str(account)[-4:]
    except Exception as err:
        account_logger.error(f"Ошибка при маскировке аккаунта: {err}", exc_info=True)
