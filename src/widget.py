from src.masks import get_mask_account, get_mask_card_number


def mask_account_card() -> str:
    """Функция выделяющая номер карты/аккаунта"""
    user_input_number = ""
    name_card_account = []
    user_input = input("Введите номер счета или карты")
    user_input_splited = user_input.split()
    for part_input in user_input_splited:
        if part_input.isdigit() == True:
            user_input_number = part_input
        else:
            name_card_account.append(part_input)
    if len(user_input_number) == 20:
        name_card_account.append(get_mask_account(user_input_number))
    elif len(user_input_number) == 16:
        name_card_account.append(get_mask_card_number(user_input_number))

    result = " ".join(name_card_account)
    return result


# print(mask_account_card())
