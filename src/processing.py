def filter_by_state(lists_user: list, state_meaning: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state
     соответствует указанному значению"""
    result_list = []
    if lists_user != []:
        for list_i in lists_user:
            state_meaning_list = list_i.get("state", 0)
            if state_meaning_list == state_meaning:
                # index_list_to_del = lists_user.index(list_i)
                # del lists_user[index_list_to_del]
                result_list.append(list_i)
    else:
        return "Введите корректные значения"
    return result_list


def sort_by_date(lists_dictionary: list, rule_sort: bool = True) -> list:
    """Функция сортирующая операции по дате"""

    lists_dictionary_sorted = sorted(lists_dictionary, key=lambda dict: dict["date"], reverse=rule_sort)
    return lists_dictionary_sorted
