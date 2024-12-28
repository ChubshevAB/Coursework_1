import json
import math
import os
import typing

from src.utils import get_data_from_excel

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "operations.xlsx"))

transactions = get_data_from_excel(file_path)


def generate_response(transactions: typing.Any) -> typing.Any:
    """Принимает на вход датафрейм и возвращает json-ответ с данными: последние 4 цифры карты, общая сумма расходов,
    кешбэк (1 рубль на каждые 100 рублей)"""

    cards_info = {}

    for transaction in transactions:
        card_number = transaction["Номер карты"]
        amount = -transaction["Сумма операции"]

        if isinstance(card_number, float) and math.isnan(card_number):
            continue

        last_digits = str(card_number)[-4:]

        if card_number not in cards_info:
            cards_info[card_number] = {
                "last_digits": last_digits,
                "total_spent": 0,
                "cashback": 0,
            }

        if (
            transaction["Сумма операции"] < 0
            and transaction["Валюта операции"] == "RUB"
            and transaction["Статус"] == "OK"
        ) and transaction["Категория"] not in ("Пополнения", "Переводы", "Бонусы"):

            total_spent = cards_info[card_number].get("total_spent", 0) + amount
            cashback = cards_info[card_number].get("cashback", 0) + amount / 100

            cards_info[card_number]["total_spent"] = round(float(total_spent), 2)
            cards_info[card_number]["cashback"] = round(float(cashback), 2)

            # cards_info[card_number]["total_spent"] += amount
            # cards_info[card_number]["cashback"] += amount / 100
            # cards_info[card_number]["total_spent"] = round(float(cards_info[card_number]["total_spent"], 2))
            # cards_info[card_number]["cashback"] = round(cards_info[card_number]["cashback"], 2)
    response = list(cards_info.values())

    return json.dumps(response, ensure_ascii=False, indent=4)


# a = generate_response(transactions)
# print(a)
