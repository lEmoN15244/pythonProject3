import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "test_account_card, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83xx xxxx 5199"),
        ("Счет 64686473678894779589", "Счет xx9589"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98xx xxxx 7658"),
        ("77788", "Введите корректный номер счета"),
        ("", "Введите корректный номер счета"),
    ],
)
def test_mask_account_card(test_account_card, expected_result):
    assert mask_account_card(test_account_card) == expected_result


@pytest.mark.parametrize(
    "date_user,expected_result_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("000", "Введите корректную дату"),
        ("", "Введите корректную дату"),
        ("2024-03-11T02:26", "11.03.2024"),
    ],
)
def test_get_date(date_user, expected_result_date):
    assert get_date(date_user) == expected_result_date
