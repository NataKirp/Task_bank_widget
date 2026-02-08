import re
import datetime
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(bank_details: str) -> str:
    """Функция принимает тип и номер карты или счета и возвращает замаскированный номер"""
    bank_details_type = "".join(re.findall(r"\D+", bank_details)).rstrip()
    bank_details_number = "".join(re.findall(r"\d", bank_details))
    if bank_details.startswith("Счет"):
        masked_number = f"{bank_details_type} {get_mask_account(bank_details_number)}"
    else:
        masked_number = (
            f"{bank_details_type} {get_mask_card_number(bank_details_number)}"
        )
    return masked_number


def get_date(input_date: str) -> str:
    """Функция принимает на вход строку с датой в формате ISO 8601 и возвращает
    строку с датой в формате 'ДД.ММ.ГГГГ'"""
    formated_date = datetime.datetime.fromisoformat(input_date)
    return formated_date.strftime("%d.%m.%Y")


if __name__ == "__main__":
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(get_date("2024-03-11T02:26:18.671407"))
