# домашняя работап 10.1
реализация модуля processing c 2мя функциями:
- filter_by_state
- sort_by_date

### пример использования:
```
# import module
import processing 

# filter list w/ dictionaries by 'state' key
test = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
print(filter_by_state(test))

print(sort_by_date(test))
```
функция filter_by_state имеет необязтельный параметр ключа сортировки: state (по умолчанию "EXECUTED")
функция sort_by_date имеет необязательный параметр сортировки по убыванию / возрастанию: reverse (по умолчанию True)


