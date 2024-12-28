import json
import os
import typing

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("apilayer_key")

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "user_settings.json"))


def load_user_currencies(file_path: str) -> typing.Any:
    """Загружает пользовательские валюты из JSON-файла."""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data.get("user_currencies", [])


def get_currency_rate(api_key: str, currencies: list) -> typing.Any:
    """Функция выводит курсы заданных валют по отношению к рублю в формате JSON."""
    rates = []

    for currency in currencies:
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency}"
        response = requests.get(url)

        if response.status_code != 200:
            continue

        data = response.json()

        if "conversion_rates" in data and "RUB" in data["conversion_rates"]:
            rub_rate = data["conversion_rates"]["RUB"]
            rates.append({"currency": currency, "rate": rub_rate})

    return json.dumps(rates, indent=2, ensure_ascii=False)


# user_currencies = load_user_currencies(file_path)
# print(user_currencies)
#
# currency_rates = get_currency_rate(api_key, user_currencies)
# print(currency_rates)
