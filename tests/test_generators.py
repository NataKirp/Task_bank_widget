from locale import currency

import pytest

from data.transactions_input import transactions
from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


# Тестирование фильтрации операций по заданной валюте
def test_filter_by_currency_valid_input(transactions_usd):
    from data.transactions_input import transactions

    result = list(filter_by_currency(transactions, "USD"))
    assert result == transactions_usd


# Тестирование работы функции при отсутствии входных данных
def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))
    assert result == []


# Тестирование работы функции при отсутствии заданной валюты в списке
def test_filter_by_currency_invalid_currency():
    with pytest.raises(ValueError):
        list(filter_by_currency(transactions, ''))


# Тестирование работы функции с некорректными типами данных
def test_filter_by_currency_wrong_type():
    with pytest.raises(TypeError):
        list(filter_by_currency("not a list", "USD"))
    with pytest.raises(TypeError):
        list(filter_by_currency([1, 2, 3], "USD"))



# Тестирование вывода описания каждой операции из списка транзакций
def test_transaction_descriptions_valid_input(operation_descriptions):
    result = list(transaction_descriptions(transactions))
    assert result == operation_descriptions


# Тестирование работы функции при отсутствии входных данных
def test_transaction_descriptions_empty_list():
    result = list(transaction_descriptions([]))
    assert result == []


# Тестирование работы функции с некорректными типами данных
def test_transaction_descriptions_dict_in_list():
    with pytest.raises(ValueError):
        list(transaction_descriptions([{"id": 1}, "not a dict"]))
    with pytest.raises(ValueError):
        list(transaction_descriptions("not a list"))


# Тестирование генерации номеров карт в заданном диапазоне
def test_card_number_generator_valid_range(card_numbers_5, start=1, stop=5):
    result = list(card_number_generator(start, stop))
    assert result == card_numbers_5


# Тестирование работы функции с неправильными значениями диапазона номеров
@pytest.mark.parametrize("start, stop", [(10, 5), (-1, 5), (-10, 5), (5, 0), (0, 0)])
def test_card_number_generator_invalid_range(start, stop):
    with pytest.raises(ValueError):
        list(card_number_generator(start, stop))


# Тестирование генерации одного номера карты
def test_card_number_generator_single_number():
    assert list(card_number_generator(9999999999999999, 9999999999999999)) == [
        "9999 9999 9999 9999"
    ]
    assert list(card_number_generator(0, 1)) == ["0000 0000 0000 0001"]
    assert list(card_number_generator(1, 1)) == ["0000 0000 0000 0001"]


# Тестирование работы функции, если одна из границ диапазона номеров превышает 16 цифр
def test_card_number_generator_over16(start=1, stop=100000000000000000):
    with pytest.raises(ValueError):
        list(card_number_generator(start, stop))
