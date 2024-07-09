from src.masks import get_mask_account, get_mask_card_number

user_card_number = input("Введите номер карты ")

if len(user_card_number) != 16:
    print("Введен некорректный номер карты ")
else:
    card_number: str = user_card_number

user_account_number = input("Введите номер счета")
if len(user_account_number) != 20:
    print("Введен некорректный номер счета")
else:
    account: str = str(user_account_number)

result_mask_card = get_mask_card_number(card_number)
result_mask_account = get_mask_account(account)
print(result_mask_card)
print(result_mask_account)
