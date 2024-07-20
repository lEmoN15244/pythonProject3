from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card

operations = []
user_list_operation = []
number = ""
user_input = input(
    """Введите какую операцию хотите выполнить?
    (максировка счета или карты/ сортировка операций/сортировка операций по дате)"""
)
if user_input == "максировка счета или карты":
    print(mask_account_card())
elif user_input == "сортировка операций по дате":
    user_list_operation = list(input("Введите список операций"))
    print(sort_by_date(user_list_operation))
elif user_input == "сортировка операций":
    operations == list(input("Введите список операций"))
    print(filter_by_state(operations))


# print(get_date(user_input))
