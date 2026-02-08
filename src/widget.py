import re
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


if __name__ == "__main__":
    print(mask_account_card("Visa Gold 5999414228426353"))
