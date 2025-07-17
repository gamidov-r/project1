def filter_by_state(dictionaries: list, state: str = "EXECUTED") -> list:
    """сортировка словарей по ключу"""
    result = []
    for item in dictionaries:
        if item.get("state") == state:
            result.append(item)
    return result


def sort_by_date(dictionaries: list, reverse: bool = True) -> list:
    """сортировка словарей по дате"""
    dictionaries.sort(reverse=reverse, key=lambda x: x.get("date"))
    return dictionaries
