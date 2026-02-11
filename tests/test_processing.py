import pytest

from src.processing import filter_by_state, sort_by_date


# Тестирование фильтрации списка по заданному статусу
@pytest.mark.parametrize("state", ["EXECUTED", "CANCELED", ""])
def test_filter_by_state(
    transactions, transactions_state_executed, transactions_state_canceled, state
):
    assert filter_by_state(transactions, "EXECUTED") == transactions_state_executed
    assert filter_by_state(transactions) == transactions_state_executed
    assert filter_by_state(transactions, "CANCELED") == transactions_state_canceled


# Тестирование работы функции при отсутствии словарей со статусом state
def test_filter_by_state_no_state(transactions_without_state):
    assert filter_by_state(transactions_without_state) == []


# Тестирование сортировки списка словарей по датам в порядке убывания, возрастания и по умолчанию.
@pytest.mark.parametrize("descending", ["False", "True", ""])
def test_sort_by_date(
    transactions, descending, sort_by_date_descending, sort_by_date_ascending
):
    assert sort_by_date(transactions, descending=True) == sort_by_date_descending
    assert sort_by_date(transactions, descending=False) == sort_by_date_ascending
    assert sort_by_date(transactions) == sort_by_date_descending


# Тестирование корректности сортировки при одинаковых датах
def test_sort_by_date_same_date(transactions_same_date):
    assert transactions_same_date == transactions_same_date


# Тестирование работы функции с некорректными или нестандартными форматами дат
def test_sort_by_date_wrong_date(transactions_wrong_date):
    with pytest.raises(ValueError):
        sort_by_date(transactions_wrong_date)
