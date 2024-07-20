def filter_by_state(lists_user: list, state_meaning: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state
     соответствует указанному значению"""
    result_list = []
    for list_i in lists_user:
        state_meaning_list = list_i.get("state", 0)
        if state_meaning_list == state_meaning:
            # index_list_to_del = lists_user.index(list_i)
            # del lists_user[index_list_to_del]
            result_list.append(list_i)
            return result_list


# lists_user = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
# print(filter_by_state(lists_user, "CANCELED"))


def sort_by_date(lists_dictionary: list, rule_sort: bool = True) -> list:
    """Функция сортирующая операции по дате"""

    lists_dictionary_sorted = sorted(lists_dictionary, key=lambda dict: dict["date"])
    return lists_dictionary_sorted


# lists_dictionary = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
# print (sort_by_date(lists_dictionary))
