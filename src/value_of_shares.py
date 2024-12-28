import json
import os
import typing

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "user_settings.json"))


def load_user_currencies_of_share(file_path: str) -> typing.Any:
    """Загружает пользовательские валюты из JSON-файла."""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data.get("user_stocks", [])


def get_price(symbols: list) -> typing.Any:
    """Получает стоимость акций по символу из S&P 500 через Alpha Vantage API."""

    stock_prices = []

    for symbol in symbols:
        url = (
            f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey="
            f"{api_key}"
        )
        response = requests.get(url)

        if response.status_code != 200:
            return {"error": f"Ошибка при получении данных для {symbol}: {response.status_code}"}

        data = response.json()

        if "Time Series (1min)" in data:
            last_refreshed = data["Meta Data"]["3. Last Refreshed"]
            stock_data = data["Time Series (1min)"][last_refreshed]
            stock_prices.append(
                {
                    "stock": symbol,
                    "price": float(stock_data["1. open"]),
                }
            )
        else:
            stock_prices.append({"stock": symbol, "price": None})

    return json.dumps(stock_prices, ensure_ascii=False, indent=4)


# symbols = load_user_currencies_of_share(file_path)
# print(symbols)
#
# result = get_price(symbols)
# print(result)
