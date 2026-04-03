from unittest.mock import patch

import pytest

from src.user_input import (description_param, display_menu,
                            process_file_choice, rub_params, sort_params)


@patch('builtins.input', return_value='1')
def test_display_menu_valid_choice(mock_input):
    result = display_menu()
    assert result == '1'
    mock_input.assert_called_once()


@patch('builtins.input', side_effect=['4', '2'])
def test_display_menu_invalid_then_valid_choice(mock_input):
    result = display_menu()
    assert result == '2'
    assert mock_input.call_count == 2


def test_json_file_choice():
    with patch('src.user_input.load_operations',
               return_value=[{'id': 1, 'name': 'Transaction 1'}]) as mock_load_operations:
        result = process_file_choice('1')
        assert result == [{'id': 1, 'name': 'Transaction 1'}]
        mock_load_operations.assert_called_once_with('data/operations.json')


def test_csv_file_choice():
    with patch(
            'src.user_input.read_csv_file', return_value=[{'id': 2, 'name': 'Transaction 2'}]
    ) as mock_read_csv_file:
        result = process_file_choice('2')
        assert result == [{'id': 2, 'name': 'Transaction 2'}]
        mock_read_csv_file.assert_called_once_with('data/transactions.csv')


def test_xlsx_file_choice():
    with patch('src.user_input.read_excel_file',
               return_value=[{'id': 3, 'name': 'Transaction 3'}]) as mock_read_excel_file:
        result = process_file_choice('3')
        assert result == [{'id': 3, 'name': 'Transaction 3'}]
        mock_read_excel_file.assert_called_once_with('data/transactions_excel.xlsx')


def test_invalid_choice():
    try:
        process_file_choice('4')
        print("Test invalid choice: FAIL")
    except KeyError:
        print("Test invalid choice: PASS")


@patch('builtins.print')
def test_sort_ascending(mock_print):
    with patch('builtins.input', side_effect=['да', 'по возрастанию']):
        assert not sort_params()


@patch('builtins.print')
def test_sort_descending(mock_print):
    with patch('builtins.input', side_effect=['да', 'по убыванию']):
        assert sort_params()


@patch('builtins.print')
def test_no_sort(mock_print):
    with patch('builtins.input', side_effect=['нет']):
        assert sort_params() is None


@patch('builtins.print')
def test_invalid_sort_choice(mock_print):
    with patch('builtins.input', side_effect=['invalid', 'да', 'по возрастанию']):
        assert not sort_params()


@patch('builtins.print')
def test_invalid_order_choice(mock_print):
    with patch('builtins.input', side_effect=['да', 'invalid', 'по возрастанию']):
        assert not sort_params()


@patch('builtins.input', return_value='Да')
def test_rub_params_valid_input(mock_input):
    result = rub_params()
    assert result == True
    mock_input.assert_called_once()


@pytest.mark.parametrize('user_choice, expected', [
    (["123", "нет"], False),
    (["нет"], False),
    (["да"], True),
    (["ДА"], True),
])
@patch('builtins.input')
def test_rub_params(mock_input, user_choice, expected):
    mock_input.side_effect = user_choice
    assert rub_params() == expected


def test_description_param_yes():
    def mock_get_input(prompt):
        if 'Да/Нет' in prompt:
            return 'да'
        else:
            return 'test_word'

    result = description_param(get_input=mock_get_input)
    assert result == 'test_word'


def test_description_param_no():
    def mock_get_input(prompt):
        return 'нет'

    result = description_param(get_input=mock_get_input)
    assert result is None
