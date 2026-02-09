import datetime
import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_details: str) -> str:
    """Функция принимает тип и номер карты или счета и возвращает замаскированный номер"""
    bank_details_type = "".join(re.findall(r"\D+", bank_details)).rstrip()
    bank_details_number = "".join(re.findall(r"\d", bank_details))
    if bank_details.startswith("Счет"):
        masked_number = f"{bank_details_type} {get_mask_account(bank_details_number)}"
    elif bank_details_type.startswith("Master") or bank_details_type.startswith("Visa") or bank_details_type.startswith("Maestro"):
        masked_number = (
            f"{bank_details_type} {get_mask_card_number(bank_details_number)}"
        )
    else:
        raise ValueError(
            "Неверное обозначение карты или счета"
        )
    return masked_number


def get_date(input_date: str) -> str:
    """Функция принимает на вход строку с датой в формате ISO 8601 и возвращает
    строку с датой в формате 'ДД.ММ.ГГГГ'"""
    try:
        formated_date = datetime.datetime.fromisoformat(input_date)
        return formated_date.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError(f"Не удалось распознать дату: {input_date}")
