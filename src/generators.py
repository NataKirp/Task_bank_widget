from typing import Generator

from data.transactions_input import transactions


def filter_by_currency(list_of_dicts: list[dict], currency_name: str):
    """
    Принимает на вход список словарей, представляющих транзакции
    и возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной.
    :param list_of_dicts: Список словарей
    :param currency_name: Ключ "name", по значению которого фильтруется список (валюта операции)
    :return: Итератор с заданным значением ключа
    """
    if not isinstance(list_of_dicts, list) or not all(isinstance(item, dict) for item in list_of_dicts):
        raise TypeError("Неправильный формат исходных данных. Ожидается список словарей")
    if not isinstance(currency_name, str) or not currency_name.strip():
        raise ValueError("Валюта операции отсутствует или у нее неверный тип")
    if not transactions:
        print("Список транзакций пуст")
        return transactions

    for item in list_of_dicts:
        try:
            if item["operationAmount"]["currency"]["name"] == currency_name:
                yield item
        except (KeyError, TypeError):
            # Пропуск словарей, в которых нет необходимых ключей или есть некорректные типы
            pass


def transaction_descriptions(list_of_dicts: list[dict]):
    """
    Принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди.
    :param list_of_dicts: Список словарей
    :return: Значение по ключу "description" (содержание операции)
    """
    if not isinstance(list_of_dicts, list) or not all(
        isinstance(i, dict) for i in list_of_dicts
    ):
        raise ValueError(
            "Неправильный формат исходных данных. Ожидается список словарей"
        )
    if not transactions:
        print("Список транзакций пуст")
        return transactions

    for i in list_of_dicts:
        if "description" in i:
            yield i["description"]
        else:
            yield f"Отсутствует содержание операции для транзакции: {i}"


def card_number_generator(start: int, stop: int) -> Generator[str]:
    """
    Генерирует номера карт в заданном диапазоне
    :param start: Число, задающее начальное значение диапазона
    :param stop: Число, задающее конечное значение диапазона
    :return: Номер карты в формате XXXX XXXX XXXX XXXX
    """
    if start > stop:
        raise ValueError("Начальное значение диапазона должно быть не больше конечного")
    if start < 0 or stop < 0:
        raise ValueError("Границы диапазона должны быть положительными числами")
    if stop == 0:
        raise ValueError("Конечное значение диапазона должно быть больше 0")
    if start > 9999999999999999 or stop > 9999999999999999:
        raise ValueError("Номер карты не может быть больше 16 цифр")
    if start == 0:
        start = 1
    for num in range(start, stop + 1):
        card_num = f"{num:0>16}"
        card_num = " ".join([card_num[i:i + 4] for i in range(0, 16, 4)])
        yield card_num


#
# if __name__ == "__main__":
#
#     usd_transactions = filter_by_currency(transactions, "USD")
#     for _ in range(5):
# print(next(usd_transactions))
#
# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
#     print(next(descriptions))
# #
# for card_number in card_number_generator(-10, -5):
#     print(card_number)
