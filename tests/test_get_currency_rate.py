import json
import typing
from unittest.mock import MagicMock, patch

import pytest

from src.get_currency_rate import get_currency_rate, load_user_currencies


@pytest.fixture()
def mock_user_settings() -> typing.Any:
    return {"user_currencies": ["USD", "EUR", "JPY"]}


def test_load_user_currencies(mocker: typing.Any, mock_user_settings: typing.Any) -> None:
    mock_open = mocker.patch("builtins.open", mocker.mock_open(read_data=json.dumps(mock_user_settings)))
    currencies = load_user_currencies("data/user_settings.json")
    assert currencies == mock_user_settings["user_currencies"]
    mock_open.assert_called_once_with("data/user_settings.json", "r", encoding="utf-8")


@patch("requests.get")
def test_get_currency_rate(mock_get: typing.Any) -> None:

    mock_response = {"conversion_rates": {"RUB": 73.21, "EUR": 87.08}}

    mock_get.return_value = MagicMock(status_code=200)
    mock_get.return_value.json.return_value = mock_response

    currencies = ["USD", "EUR"]

    result = get_currency_rate("fake_api_key", currencies)

    expected_result = {
        "currency_rates": [
            {"currency": "USD", "rate": 73.21},
            {"currency": "EUR", "rate": 73.21},
        ]
    }

    assert result == expected_result
    mock_get.assert_called_with("https://v6.exchangerate-api.com/v6/fake_api_key/latest/EUR")
