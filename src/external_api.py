import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_transaction_amount_rub(transaction: dict) -> float:
    """
    Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.
    :param transaction: Содержание транзакции в виде списка словарей
    :return: Сумма операции в рублях
    """
    amount_rub = transaction["operationAmount"]["amount"]
    if transaction["operationAmount"]["currency"]["code"] != "руб.":
        try:
            currency_name = transaction["operationAmount"]["currency"]["code"]
            url = f"https://api.apilayer.com/currency_data/convert?to=RUB&from={currency_name}&amount={amount_rub}"
            api_key = os.getenv("API_KEY")
            headers = {"apikey": api_key}
            response = requests.request("GET", url=url, headers=headers)
            response.raise_for_status()  # возвращаем исключение если код ошибки не 200
            result = response.json()
            amount_rub = float(result["result"])
        except requests.RequestException as e:
            print(f"Ошибка запроса: Код: {e}")
            return 0.0
        except Exception as e:
            print(f"Ошибка: Код: {e}")
            return 0.0

    return amount_rub

# if __name__ == '__main__':
#     transaction = {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {
#             "amount": "9824.07",
#             "currency": {"name": "USD", "code": "USD"},
#         },
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702",
#     }
#     print(get_transaction_amount_rub(transaction))
