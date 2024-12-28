import json
import typing
from unittest.mock import MagicMock, mock_open, patch

import pytest

from src.value_of_shares import get_price, load_user_currencies


@pytest.fixture
def mock_user_settings() -> typing.Any:
    return {"user_stocks": ["AAPL", "AMZN", "MSFT"]}


def test_load_user_currencies(mocker: typing.Any, mock_user_settings: typing.Any) -> None:

    mock_open_file = mocker.patch("builtins.open", mock_open(read_data=json.dumps(mock_user_settings)))

    currencies = load_user_currencies("dummy_path")

    assert currencies == mock_user_settings["user_stocks"]
    mock_open_file.assert_called_once_with("dummy_path", "r", encoding="utf-8")


@patch("requests.get")
def test_get_price(mock_get: typing.Any) -> None:

    stock_data_response = {
        "Meta Data": {"3. Last Refreshed": "2022-05-11 15:59:00"},
        "Time Series (1min)": {
            "2022-05-11 15:59:00": {
                "1. open": "150.12",
                "2. high": "151.00",
                "3. low": "149.50",
                "4. close": "150.00",
                "5. volume": "200000",
            }
        },
    }

    mock_get.return_value = MagicMock(status_code=200)
    mock_get.return_value.json.return_value = stock_data_response

    symbols = ["AAPL", "AMZN"]
    result = get_price(symbols)

    expected_result = [{"stock": "AAPL", "price": 150.12}, {"stock": "AMZN", "price": 150.12}]

    assert json.loads(result) == expected_result
