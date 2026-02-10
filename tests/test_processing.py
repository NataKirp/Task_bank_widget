import pytest

from src.processing import filter_by_state
from tests.conftest import transactions


# Тестирование фильтрации списка по заданному статусу
@pytest.mark.parametrize("state", ["EXECUTED",
                                   "CANCELED",
                                   ""])
def test_filter_by_state(transactions, transactions_state_executed, transactions_state_canceled, state):
    assert filter_by_state(transactions, "EXECUTED") == transactions_state_executed
    assert filter_by_state(transactions) == transactions_state_executed
    assert filter_by_state(transactions, "CANCELED") == transactions_state_canceled


# Тестирование работы функции при отсутствии словарей со статусом state
def test_filter_by_state_no_state(transactions_without_state):
    assert filter_by_state(transactions_without_state) == []
