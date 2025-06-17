def filter_by_state(dictionaries: list, state='EXECUTED') -> list:
    result = []
    for i in dictionaries:
        if i.get('state') == state:
            result.append(i)
    return result

# Выход функции со статусом по умолчанию 'EXECUTED'
a=[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Выход функции, если вторым аргументов передано 'CANCELED'
b=[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
print(filter_by_state(a))