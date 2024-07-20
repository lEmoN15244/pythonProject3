from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input) -> str:
    """Функция выделяющая номер карты/аккаунта"""
    user_input_number = ""
    name_card_account = []
    user_input_splited = user_input.split()
    for part_input in user_input_splited:
        if part_input.isdigit():
            user_input_number = part_input
        else:
            name_card_account.append(part_input)
    if len(user_input_number) == 20:
        name_card_account.append(get_mask_account(user_input_number))
    elif len(user_input_number) == 16:
        name_card_account.append(get_mask_card_number(user_input_number))
    else:
        return "Введите корректный номер счета"

    result = " ".join(name_card_account)
    return result


def get_date(user_date: str) -> str:

    if len(user_date) >= 10:
        index_time = user_date.find("T")
        date = user_date[:index_time]
        year_month_day = date.split("-")
        year_month_day.reverse()
        date_right = ".".join(year_month_day)
        return date_right
    else:
        return "Введите корректную дату"


# print(get_date("2024-03-11T02:26:18.671407"))
