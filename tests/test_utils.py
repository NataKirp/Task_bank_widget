from unittest.mock import mock_open, patch

from src.utils import (load_operations, process_bank_operations,
                       process_bank_search)


# Тестирование работы функции при отсутствии JSON-файла
def test_file_not_found(capsys):
    assert load_operations('non_existent_file.json') == []
    captured = capsys.readouterr()
    assert 'Файл не найден' in captured.out


# Тестирование работы функции, если JSON-файл пустой
def test_empty_file(tmp_path):
    empty_file = tmp_path / 'empty.json'
    empty_file.write_text('')
    assert load_operations(empty_file) == []


# Тестирование успешной работы функции
@patch('builtins.open', new_callable=mock_open, read_data='[{"key": "value"}]')
@patch('os.path.exists')
@patch('os.path.getsize')
def test_load_operations_returns_list(mock_getsize, mock_exists, mock_open):
    mock_exists.return_value = True
    mock_getsize.return_value = 1  # Предполагаем, что файл не пустой
    result = load_operations('test_file.json')
    assert isinstance(result, list)


# Тестирование работы функции, если JSON-файл содержите не список
@patch('os.path.exists', return_value=True)  # имитирует, что файл существует
@patch('os.path.getsize', return_value=1)  # имитирует, что файл не пустой
@patch('builtins.open', create=True)
def test_load_operations_not_list(mock_open, mock_getsize, mock_exists):
    mock_file = mock_open.return_value.__enter__.return_value  # имитирует with open
    mock_file.read.return_value = '{"key": "value"}'  # вызов метода read возвращает словарь
    assert load_operations('test.json') == []


def test_process_bank_search():
    # Есть операции, подходящие под описание
    data = [
        {'description': 'Test operation 1'},
        {'description': 'Another test operation'},
        {'description': 'Not matching'}
    ]
    search = 'test'
    expected = [
        {'description': 'Test operation 1'},
        {'description': 'Another test operation'}
    ]
    assert process_bank_search(data,
                               search) == expected, f"Expected {expected} but got {process_bank_search(data, search)}"

    # Нет операций, подходящих под описание
    data = [
        {'description': 'Operation 1'},
        {'description': 'Another operation'}
    ]
    search = 'test'
    expected = []
    assert process_bank_search(data,
                               search) == expected, f"Expected {expected} but got {process_bank_search(data, search)}"

    # Пустой список с исходными данными
    data = []
    search = 'test'
    expected = []
    assert process_bank_search(data,
                               search) == expected, f"Expected {expected} but got {process_bank_search(data, search)}"

    # Пустая строка поиска
    data = [
        {'description': 'Test operation 1'},
        {'description': 'Another test operation'}
    ]
    search = ''
    expected = data
    assert process_bank_search(data,
                               search) == expected, f"Expected {expected} but got {process_bank_search(data, search)}"

    # Неправильное описание
    data = [
        {'id': 1},
        {'description': 'Test operation'}
    ]
    search = 'test'
    expected = [
        {'description': 'Test operation'}
    ]
    assert process_bank_search(data,
                               search) == expected, f"Expected {expected} but got {process_bank_search(data, search)}"


def test_process_bank_operations():
    # Пустой список с исходными данными
    data = []
    categories = ['category1', 'category2']
    assert process_bank_operations(data, categories) == {}

    # Нет подходящих категорий
    data = [{'description': 'category3'}, {'description': 'category4'}]
    categories = ['category1', 'category2']
    assert process_bank_operations(data, categories) == {}

    # Есть категории для группировки
    data = [{'description': 'category1'}, {'description': 'category2'}, {'description': 'category1'}]
    categories = ['category1', 'category2']
    assert process_bank_operations(data, categories) == {'category1': 2, 'category2': 1}
