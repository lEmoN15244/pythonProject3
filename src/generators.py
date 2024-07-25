import random
import textwrap
from random import randint

transactions = [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод организации", "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"},
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }]

def filter_by_currency(transactions, currency_name="USD"):
    """Функция выдает транзакции, где операция соответсвует заданному параметру"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == currency_name:
             yield transaction



# usd_transactions = filter_by_currency(transactions, "USD")
# for i in range(2):
#     print(next(usd_transactions))

def transaction_descriptions(transactions):
    """Генератор выдающий описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction['description']

# descriptions = transaction_descriptions(transactions)
# for i in range(2):
#     print(next(descriptions))


def card_number_generator():
    while True:
        number = str(random.randint(0000000000000000, 9999999999999999))
        card_number = textwrap.wrap(number, 4)
        result_card_number = " ".join(card_number)
        yield card_number



