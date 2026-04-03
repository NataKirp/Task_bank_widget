import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тестирование правильности маскирования номера карты
def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("1234567891561234") == "1234 56** **** 1234"
    assert get_mask_card_number("0000000000000000") == "0000 00** **** 0000"


# Тестирование обработки нестандартных длин номеров и отсутствия номера
@pytest.mark.parametrize(
    "card_number",
    [
        "123456789",
        "0000",
        "5",
        "123456789123456789",
        "счет 1234 5678 9123 4567",
        "visa1234567891234567",
        "2815-3218-8816-4547",
        "2815 3218 8816 4547",
        "",
    ],
)
def test_get_mask_card_number_invalid_or_no_number(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


# Тестирование правильности маскирования номера счета
def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("00000000000000000000") == "**0000"
    assert get_mask_account("99998888777766665555") == "**5555"


# Тестирование обработки неправильных форматов и длин номера счета
@pytest.mark.parametrize(
    "account_number",
    [
        "123456789",
        "0000",
        "5",
        "123456789123456789",
        "счет 1234 5678 9123 4567",
        "visa1234567891234567",
        "28153-21888-16454-78910",
        "2815.3218.8816.4547",
        "",
    ],
)
def test_get_mask_account_wrong_number(account_number):
    with pytest.raises(ValueError):
        get_mask_account(account_number)
