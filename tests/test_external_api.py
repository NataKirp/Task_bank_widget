from unittest.mock import Mock, patch

import requests

from src.external_api import get_transaction_amount_rub


def test_rub_currency():
    result = get_transaction_amount_rub({"operationAmount": {"amount": "43318.34", "currency": {"code": "RUB"}}})
    assert result == 43318.34


@patch('requests.request')
def test_non_rub_currency(mock_request):
    mock_response = Mock()
    mock_response.json.return_value = {'result': 778683.7868}
    mock_response.raise_for_status = Mock()
    mock_request.return_value = mock_response
    result = get_transaction_amount_rub(
        {"operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}}})
    assert result == 778683.7868


@patch('requests.request')
def test_request_exception(mock_request):
    mock_request.side_effect = requests.RequestException('Mocked error')
    result = get_transaction_amount_rub(
        {"operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}}})
    assert result == 0.0


@patch('requests.request')
def test_other_exception(mock_request):
    mock_response = Mock()
    mock_response.json.side_effect = Exception('Mocked error')
    mock_response.raise_for_status = Mock()
    mock_request.return_value = mock_response
    result = get_transaction_amount_rub(
        {"operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}}})
    assert result == 0.0
