import textwrap


def get_mask_card_number(card_number: str) -> str:
    """Функция маскирующая часть цифр номера карты"""
    card_number_str = str(card_number)
    if len(card_number_str) == 16:
        replace_part_number = card_number_str[6:-4]
        mask_number = card_number_str.replace(replace_part_number, "xxxxxx")
        bloks_masks_number = textwrap.wrap(mask_number, 4)
        result = " ".join(bloks_masks_number)
        return result
    else:
        return "Введите корректный номер карты"

# print(get_mask_card_number("7000792289606361"))
def get_mask_account(account: str) -> str:
    """Функция выводящая маску номера счета"""
    if len(account) == 20:
        return "xx" + account[-4:]
    else:
        return "Введите корректный номер счета"


# print(get_mask_account("73654108430135874305"))
