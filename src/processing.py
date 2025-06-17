def filter_by_state(dictionaries: list, state: str = "EXECUTED") -> list:
    """сортировка словарей по ключу"""
    result = []
    for i in dictionaries:
        if i.get("state") == state:
            result.append(i)
    return result


def sort_by_date(dictionaries: list, reverse: bool = True) -> list:
    """сортировка словарей по дате"""
    dictionaries.sort(reverse=True, key=lambda x: x.get("date"))
    return dictionaries
