import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "test_card_number, expected_result",
    [
        ("7000792289606361", "7000 79xx xxxx 6361"),
        ("1254458774588965", "1254 45xx xxxx 8965"),
        ("77788", "Введите корректный номер карты"),
        ("", "Введите корректный номер карты"),
    ],
)
def test_get_mask_card_number(test_card_number, expected_result):
    assert get_mask_card_number(test_card_number) == expected_result


@pytest.mark.parametrize(
    "test_account, expected_result",
    [
        ("73654108430135874305", "xx4305"),
        ("12345487896575489658", "xx9658"),
        ("77788", "Введите корректный номер счета"),
        ("", "Введите корректный номер счета"),
    ],
)
def test_get_mask_account(test_account, expected_result):
    assert get_mask_account(test_account) == expected_result
