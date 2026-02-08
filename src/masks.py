from typing import Union

# Определены константы для длины номера карты и счета
CARD_NUMBER_LENGTH = 16
ACC_NUMBER_MIN_LENGTH = 6


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Маска отображается в формате XXXX XX** **** XXXX, где X — это цифра номера."""
    card_number = str(card_number)
    # Проверка, что номер карты корректный и состоит из CARD_NUMBER_LENGTH цифр
    if len(card_number) != CARD_NUMBER_LENGTH or not card_number.isdigit():
        raise ValueError(
            "Неверный номер карты: '{card_number}'. Ожидаемый формат: {CARD_NUMBER_LENGTH} цифр."
        )

    mask_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return mask_number


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера.
    """
    account_number = str(account_number)
    # Проверка, что номер счета корректный и содержит не менее ACC_NUMBER_MIN_LENGTH цифр
    if len(account_number) < ACC_NUMBER_MIN_LENGTH or not account_number.isdigit():
        raise ValueError(
            "Неверный номер счета: '{account_number}'. Ожидаемый формат: не менее {ACCOUNT_NUMBER_MIN_LENGTH} цифр."
        )

    mask_account = f"**{account_number[-4:]}"
    return mask_account


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
