from unittest.mock import mock_open, patch

import pandas as pd

from src.file_readers import read_csv_file, read_excel_file


def test_read_csv_file():
    mock_csv_data = "id;state\n650703;EXECUTED\n593027;CANCELED"
    with patch('builtins.open', mock_open(read_data=mock_csv_data)):
        result = read_csv_file('fake_path.csv')
    assert result == [{'id': 650703, 'state': 'EXECUTED'}, {'id': 593027, 'state': 'CANCELED'}]


@patch('pandas.read_excel')
def test_read_excel_file(mock_read_excel):
    data = {'id': [650703, 593027], 'state': ['EXECUTED', 'CANCELED']}
    df = pd.DataFrame(data)
    mock_read_excel.return_value = df
    file_path = 'fake_path.xlsx'
    expected = [{'id': 650703, 'state': 'EXECUTED'}, {'id': 593027, 'state': 'CANCELED'}]
    assert read_excel_file(file_path) == expected
    mock_read_excel.assert_called_once_with(file_path)
