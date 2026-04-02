import datetime
import re

from src.masks import get_mask_account, get_mask_card_number

CARD_NUMBER_LENGTH = 16


def mask_account_card(bank_details: str) -> str:
    """Функция принимает тип и номер карты или счета и возвращает замаскированный номер"""
    if bank_details == '':
        return 'нет данных'

    bank_details_type = "".join(re.findall(r"[a-zA-Z]+\s|^МИР|^Счет", bank_details)).rstrip()
    bank_details_number = "".join(re.findall(r"\d", bank_details))
    if bank_details.startswith("Счет"):
        masked_number = f"{bank_details_type} {get_mask_account(bank_details_number)}"
    elif len(bank_details_number) == CARD_NUMBER_LENGTH:
        masked_number = f"{bank_details_type} {get_mask_card_number(bank_details_number)}"
    else:
        raise ValueError("Неверное обозначение карты или счета")
    return masked_number


def get_date(input_date: str) -> str:
    """Функция принимает на вход строку с датой в формате ISO 8601 и возвращает
    строку с датой в формате 'ДД.ММ.ГГГГ'"""
    try:
        formated_date = datetime.datetime.fromisoformat(input_date)
        return formated_date.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError(f"Не удалось распознать дату: {input_date}")
