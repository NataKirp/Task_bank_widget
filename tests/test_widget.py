import pytest

from src.widget import mask_account_card, get_date


# Тестирование правильности маскирования номера карты или счета при корректном вводе
def test_mask_account_card():
    assert mask_account_card('Счет 73654108430135874305') == 'Счет **4305'
    assert mask_account_card('Visa Platinum 7000792289606361') == 'Visa Platinum 7000 79** **** 6361'
    assert mask_account_card('MasterCard 7158300734726758') == 'MasterCard 7158 30** **** 6758'
    assert mask_account_card('Visa Gold 5999414228426353') == 'Visa Gold 5999 41** **** 6353'
    assert mask_account_card('Visa Classic 6831982476737658') == 'Visa Classic 6831 98** **** 7658'


# Тестирование обработки нестандартных номеров и отсутствия номера
@pytest.mark.parametrize('bank_details', ['Schet 73654108430135874305',
                                          'Виза Голд 5999414228426353',
                                          'Счет 71583007347267585999414228426353',
                                          'Счет 73654',
                                          'Счет 0',
                                          'Счет ',
                                          'Visa Platinum 70007922896063616831982476737658'
                                          'Visa Platinum 70007',
                                          'Visa Classic ',
                                          '73654108430135874305',
                                          ''])
def test_mask_account_card_wrong_number(bank_details):
    with pytest.raises(ValueError):
        mask_account_card(bank_details)

# Тестирование правильности обработки даты при корректном вводе
def test_get_date():
    assert get_date('2024-03-11T02:26:18.671407') == '11.03.2024'# Тестирование правильности обработки даты при корректном вводе

# Тестирование правильности обработки даты при некорректном вводе
@pytest.mark.parametrize('input_date',['20202025',
                                       '1/1/2026',
                                       '15.08.25',
                                       'Wed, 12 April 2023'
                                       ])
def test_get_date_wrong_date(input_date):
    with pytest.raises(ValueError):
        get_date(input_date)