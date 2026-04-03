from typing import Union

from src.logging_config import setup_logging

# Определены константы для длины номера карты и счета
CARD_NUMBER_LENGTH = 16
ACC_NUMBER_LENGTH = 20

masks_logger = setup_logging('masks')


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Маска отображается в формате XXXX XX** **** XXXX, где X — это цифра номера."""
    masks_logger.info('Начало работы функции get_mask_card_number')
    card_number = str(card_number)

    masks_logger.info(f'Проверка, что номер карты корректный и состоит из {CARD_NUMBER_LENGTH} цифр')
    if len(card_number) != CARD_NUMBER_LENGTH or not card_number.isdigit():
        masks_logger.error(f"Неверный номер карты: '{card_number}'. Ожидаемый формат: {CARD_NUMBER_LENGTH} цифр.")
        raise ValueError(
            f"Неверный номер карты: '{card_number}'. Ожидаемый формат: {CARD_NUMBER_LENGTH} цифр."
        )
    masks_logger.info('Номер карты замаскирован')
    mask_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    masks_logger.info('Завершение работы функции get_mask_card_number')
    return mask_number


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера.
    """
    masks_logger.info('Начало работы функции get_mask_account')
    account_number = str(account_number)
    masks_logger.info(f'Проверка, что номер счета корректный и состоит из {ACC_NUMBER_LENGTH} цифр')
    if len(account_number) != ACC_NUMBER_LENGTH or not account_number.isdigit():
        masks_logger.error(f"Неверный номер счета: '{account_number}'. Ожидаемый формат: {ACC_NUMBER_LENGTH} цифр.")
        raise ValueError(
            f"Неверный номер счета: '{account_number}'. Ожидаемый формат: {ACC_NUMBER_LENGTH} цифр."
        )
    masks_logger.info('Номер счета замаскирован')
    mask_account = f"**{account_number[-4:]}"
    masks_logger.info('Завершение работы функции get_mask_account')
    return mask_account


# if __name__ == '__main__':
#     mask_number = get_mask_card_number("7000792289606361")
#     mask_account = get_mask_account("73654108430135874305")
#     print(mask_number)
#     print(mask_account)
